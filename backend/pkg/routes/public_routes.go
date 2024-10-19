package routes

import (
	"github.com/Lemon-Corporation/worlds.chat/backend/app/controllers"
	"github.com/gofiber/fiber/v2"
	"github.com/jmoiron/sqlx"
)

func PublicRoutes(a *fiber.App, db *sqlx.DB) {
	route := a.Group("/api/v1")

	userController := controllers.NewUserController(db)

	route.Post("/user/sign/up", userController.UserSignUp)
	route.Post("/user/sign/in", userController.UserSignIn)
	route.Post("/user/sign/out", userController.UserSignOut)
	route.Post("/user/renew/tokens", userController.RenewTokens)

	// Оставляем существующие маршруты для книг
	route.Get("/books", controllers.GetBooks)
	route.Get("/book/:id", controllers.GetBook)
}
