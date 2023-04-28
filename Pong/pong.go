package main

import (
	"image/color"
	"log"
	"math"
	"math/rand"
	"time"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

const (
	ScreenWidth    = 640
	ScreenHeight   = 480
	PaddleWidth    = 20
	PaddleHeight   = 80
	BallSize       = 20
	BallSpeed      = 5
	OpponentSpeed  = 3
	InitialDelay   = 60
	BounceAngle    = 45
	BounceAngleRad = BounceAngle * (math.Pi / 180)
)

var (
	player1Y     = ScreenHeight / 2
	player1Speed = 5
	opponentY    = ScreenHeight / 2
	ballX, ballY = ScreenWidth / 2, ScreenHeight / 2
	ballDX       = BallSpeed * math.Cos(BounceAngleRad)
	ballDY       = BallSpeed * -math.Sin(BounceAngleRad)
)

type Game struct{}

func (g *Game) Update() error {
	// Move the player's paddle
	if ebiten.IsKeyPressed(ebiten.KeyW) && player1Y > 0 {
		player1Y -= player1Speed
	}
	if ebiten.IsKeyPressed(ebiten.KeyS) && player1Y < ScreenHeight-PaddleHeight {
		player1Y += player1Speed
	}

	// Move the opponent's paddle
	if ballY < opponentY+(PaddleHeight/2) && opponentY > 0 {
		opponentY -= OpponentSpeed
	}
	if ballY > opponentY+(PaddleHeight/2) && opponentY < ScreenHeight-PaddleHeight {
		opponentY += OpponentSpeed
	}

	// Update the ball's position
	ballX += int(ballDX)
	ballY += int(ballDY)

	// Check collisions with paddles
	if ballX <= PaddleWidth && ballY >= player1Y && ballY <= player1Y+PaddleHeight {
		ballDX = math.Abs(ballDX)
		ballDY = ballDY * -1
	}
	if ballX >= ScreenWidth-BallSize-PaddleWidth && ballY >= opponentY && ballY <= opponentY+PaddleHeight {
		ballDX = -math.Abs(ballDX)
		ballDY = ballDY * -1
	}

	// Check collisions with walls
	if ballY <= 0 || ballY >= ScreenHeight-BallSize {
		ballDY = -ballDY
	}

	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	screen.Fill(color.Black)

	// Draw player's paddle
	ebitenutil.DrawRect(screen, PaddleWidth, float64(player1Y), PaddleWidth, PaddleHeight, color.White)

	// Draw opponent's paddle
	ebitenutil.DrawRect(screen, ScreenWidth-PaddleWidth*2, float64(opponentY), PaddleWidth, PaddleHeight, color.White)

	// Draw ball
	ebitenutil.DrawRect(screen, float64(ballX), float64(ballY), BallSize, BallSize, color.White)
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (int, int) {
	return ScreenWidth, ScreenHeight
}

func main() {
	ebiten.SetWindowSize(ScreenWidth, ScreenHeight)
	ebiten.SetWindowTitle("Pong Game")

	rand.Seed(time.Now().UnixNano())

	log.Println("Starting the game...")

	game := &Game{}
	if err := ebiten.RunGame(game); err != nil {
		log.Fatal("Error: ", err)
	}
}
