const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const box = 20;
let snake, food, direction, score, game;

function init() {
  snake = [{ x: 9 * box, y: 9 * box }];
  food = { x: Math.floor(Math.random() * 20) * box, y: Math.floor(Math.random() * 20) * box };
  direction = null;
  score = 0;
  document.getElementById("score").innerText = score;
  document.getElementById("gameOverModal").classList.add("hidden");
  if (game) clearInterval(game);
  game = setInterval(draw, 100);
  document.getElementById("highScore").innerText = localStorage.getItem("snakeHigh") || 0;
}

function draw() {
  ctx.fillStyle = "#1e293b";
  ctx.fillRect(0, 0, 400, 400);

  // Draw snake
  snake.forEach((part, i) => {
    ctx.fillStyle = i === 0? "#22c55e" : "#86efac";
    ctx.fillRect(part.x, part.y, box - 2, box - 2);
  });

  // Draw food
  ctx.fillStyle = "#ef4444";
  ctx.fillRect(food.x, food.y, box - 2, box - 2);

  let headX = snake[0].x;
  let headY = snake[0].y;

  if (direction === "left") headX -= box;
  if (direction === "up") headY -= box;
  if (direction === "right") headX += box;
  if (direction === "down") headY += box;

  // Wall collision + Self collision -> Game Over
  if (headX < 0 || headY < 0 || headX >= 400 || headY >= 400 || collision(headX, headY, snake)) {
    return gameOver();
  }

  // Eat food
  if (headX === food.x && headY === food.y) {
    score++;
    document.getElementById("score").innerText = score;
    food = { x: Math.floor(Math.random() * 20) * box, y: Math.floor(Math.random() * 20) * box };
  } else {
    snake.pop();
  }

  snake.unshift({ x: headX, y: headY });
}

function collision(x, y, array) {
  return array.some(part => part.x === x && part.y === y);
}

function changeDirection(dir) {
  const opposite = { up: "down", down: "up", left: "right", right: "left" };
  if (opposite[dir]!== direction) direction = dir;
}

document.addEventListener("keydown", e => {
  if (e.key === "ArrowLeft") changeDirection("left");
  if (e.key === "ArrowUp") changeDirection("up");
  if (e.key === "ArrowRight") changeDirection("right");
  if (e.key === "ArrowDown") changeDirection("down");
});

function gameOver() {
  clearInterval(game);
  document.getElementById("finalScore").innerText = score;
  document.getElementById("gameOverModal").classList.remove("hidden");

  let high = localStorage.getItem("snakeHigh") || 0;
  if (score > high) {
    localStorage.setItem("snakeHigh", score);
    document.getElementById("highScore").innerText = score;
  }
}

function restartGame() { init(); }

init();