package main

import (
	"fmt"
	"log"
	"os"

	"github.com/Lemon-Corporation/worlds.chat/backend/pkg/configs"
	"github.com/Lemon-Corporation/worlds.chat/backend/pkg/middleware"
	"github.com/Lemon-Corporation/worlds.chat/backend/pkg/routes"
	"github.com/Lemon-Corporation/worlds.chat/backend/pkg/utils"

	"github.com/gofiber/fiber/v2"
	"github.com/jmoiron/sqlx"

	_ "github.com/Lemon-Corporation/worlds.chat/backend/docs" // load API Docs files (Swagger)
	_ "github.com/lib/pq"                                     // PostgreSQL driver

	_ "github.com/joho/godotenv/autoload" // load .env file automatically
)

// @title API
// @version 1.0
// @description This is an auto-generated API Docs.
// @termsOfService http://swagger.io/terms/
// @contact.name API Support
// @contact.email your@mail.com
// @license.name Apache 2.0
// @license.url http://www.apache.org/licenses/LICENSE-2.0.html
// @BasePath /api
// @securityDefinitions.apikey ApiKeyAuth
// @in header
// @name Authorization
func main() {
	// Connect to the database
	db, err := connectDB()
	if err != nil {
		log.Fatalf("Failed to connect to database: %v", err)
	}
	defer db.Close()

	// Define Fiber config.
	config := configs.FiberConfig()

	// Define a new Fiber app with config.
	app := fiber.New(config)

	// Middlewares.
	middleware.FiberMiddleware(app) // Register Fiber's middleware for app.

	// Routes.
	routes.SwaggerRoute(app)      // Register a route for API Docs (Swagger).
	routes.PublicRoutes(app, db)  // Register public routes for app, passing the db connection.
	routes.PrivateRoutes(app, db) // Register private routes for app.
	routes.NotFoundRoute(app)     // Register route for 404 Error.

	// Start server (with or without graceful shutdown).
	if os.Getenv("STAGE_STATUS") == "dev" {
		utils.StartServer(app)
	} else {
		utils.StartServerWithGracefulShutdown(app)
	}
}

func connectDB() (*sqlx.DB, error) {
	dbURL := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		os.Getenv("DB_HOST"),
		os.Getenv("DB_PORT"),
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_NAME"),
	)

	return sqlx.Connect("postgres", dbURL)
}
