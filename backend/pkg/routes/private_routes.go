package routes

import (
	"github.com/Lemon-Corporation/worlds.chat/backend/app/controllers"
	"github.com/Lemon-Corporation/worlds.chat/backend/pkg/middleware"
	"github.com/gofiber/fiber/v2"
	"github.com/jmoiron/sqlx"
)

// PrivateRoutes func for describe group of private routes.
func PrivateRoutes(a *fiber.App, db *sqlx.DB) {
	// Create routes group.
	route := a.Group("/api/v1")

	// Initialize UserController
	userController := controllers.NewUserController(db)

	// Routes for POST method:
	route.Post("/book", middleware.JWTProtected(), controllers.CreateBook)              // create a new book
	route.Post("/user/sign/out", middleware.JWTProtected(), userController.UserSignOut) // de-authorization user
	route.Post("/token/renew", middleware.JWTProtected(), userController.RenewTokens)   // renew Access & Refresh tokens

	// Routes for PUT method:
	route.Put("/book", middleware.JWTProtected(), controllers.UpdateBook) // update one book by ID

	// Routes for DELETE method:
	route.Delete("/book", middleware.JWTProtected(), controllers.DeleteBook) // delete one book by ID
}
