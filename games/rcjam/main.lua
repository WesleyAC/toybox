function love.load()
  math.randomseed( os.time() )
  love.physics.setMeter(64)
  world = love.physics.newWorld(0, 9.81*64, true)
  world:setCallbacks(beginContact, endContact, preSolve, postSolve)

  score = 0

  can_jump = true
  touching_ground = true
  jumpcountdown = 0.25

  objectfallcountdown = 5.0
  objectfalltime = 5.0

  gameover = false

  shit = {}

  objects = {}

  objects.ball = {}
  objects.ball.body = love.physics.newBody(world, 400, 550, "dynamic")
  objects.ball.shape = love.physics.newCircleShape(20)
  objects.ball.fixture = love.physics.newFixture(objects.ball.body, objects.ball.shape, 150)
  objects.ball.fixture:setRestitution(0.9)
  objects.ball.body:setLinearDamping(1)

  objects.feet = {}
  objects.feet.body = love.physics.newBody(world, 400, 560, "dynamic")
  objects.feet.shape = love.physics.newRectangleShape(0, 0, 35, 22)
  objects.feet.fixture = love.physics.newFixture(objects.feet.body, objects.feet.shape, 0)
  objects.feet.fixture:setUserData("feet")

  objects.pivot = {}
  objects.pivot.body = love.physics.newBody(world, 400, 600)
  objects.pivot.shape = love.physics.newPolygonShape(-25, 0, 0, -25, 25, 0)
  objects.pivot.fixture = love.physics.newFixture(objects.pivot.body, objects.pivot.shape)

  objects.scale = {}
  objects.scale.body = love.physics.newBody(world, 400, 575, "dynamic")
  objects.scale.shape = love.physics.newRectangleShape(0, 0, 500, 10)
  objects.scale.fixture = love.physics.newFixture(objects.scale.body, objects.scale.shape, 2000)

  love.physics.newRevoluteJoint(objects.pivot.body, objects.scale.body, 400, 575, false)
  love.physics.newWeldJoint(objects.ball.body, objects.feet.body, 400, 560, false)

  love.graphics.setBackgroundColor(104, 136, 248)
end


function love.update(dt)
  world:update(dt)

  score = score + dt

  if objects.ball.body:getY() > 800 then
    gameover = true
  end

  objectfallcountdown = objectfallcountdown - dt

  if objectfallcountdown <= 0.0 then
    table.insert(shit,
      love.physics.newFixture(
        love.physics.newBody(world, 300 + (math.random() * 400), 0, "dynamic"),
        love.physics.newRectangleShape(0,0,50,50),
        10))
    objectfalltime = objectfalltime * 0.9
    objectfallcountdown = objectfalltime
  end

  if not touching_ground then
    jumpcountdown = jumpcountdown - dt
    if jumpcountdown <= 0 then
      can_jump = false
    else
      can_jump = true
    end
  else
    can_jump = true
  end

  if love.keyboard.isDown("right") then
    objects.ball.body:applyForce(10000, 0)
  end
  if love.keyboard.isDown("left") then
    objects.ball.body:applyForce(-10000, 0)
  end
  if love.keyboard.isDown("up") and can_jump then
    objects.ball.body:setLinearVelocity(objects.ball.body:getLinearVelocity(), -300)
  end
end

function love.draw()
  if not gameover then
    love.graphics.print("SCORE: " .. round(score, 1), 10, 10, 0, 1, 1, 0, 0, 0, 0)
    -- draw ball
    love.graphics.setColor(193, 47, 14)
    love.graphics.circle("fill", objects.ball.body:getX(), objects.ball.body:getY(), objects.ball.shape:getRadius())
    fear = math.abs(objects.scale.body:getAngle()) * 2;
    love.graphics.setColor(255, 255, 255)
    love.graphics.circle("fill", objects.ball.body:getX() - 7, objects.ball.body:getY() - 8, 5 + (2 * fear))
    love.graphics.circle("fill", objects.ball.body:getX() + 7, objects.ball.body:getY() - 8, 5 + (2 * fear))
    love.graphics.setColor(0, 0, 0)
    love.graphics.circle("fill", objects.ball.body:getX() - 7, objects.ball.body:getY() - 8, 1 + (3 * fear))
    love.graphics.circle("fill", objects.ball.body:getX() + 7, objects.ball.body:getY() - 8, 1 + (3 * fear))

    love.graphics.setColor(50, 50, 50)
    love.graphics.polygon("fill", objects.pivot.body:getWorldPoints(objects.pivot.shape:getPoints()))
    love.graphics.polygon("fill", objects.scale.body:getWorldPoints(objects.scale.shape:getPoints()))

    for useless,thing in pairs(shit) do
      love.graphics.polygon("fill", thing:getBody():getWorldPoints(thing:getShape():getPoints()))
    end
  else
    love.graphics.print("GAME OVER!", 10, 10, 0, 1, 1, 0, 0, 0, 0)
  end
end

function beginContact(a, b, coll)
  if (a:getUserData() == "feet" or b:getUserData() == "feet") then
    touching_ground = true
    jumpcountdown = 0.25
  end
end

function endContact(a, b, coll)
  if (a:getUserData() == "feet" or b:getUserData() == "feet") then
    touching_ground = false
    jumpcountdown = 0.25
  end
end

function preSolve(a, b, coll)

end

function postSolve(a, b, coll, normalimpulse, tangentimpulse)

end

function round(num, numDecimalPlaces)
  local mult = 10^(numDecimalPlaces or 0)
  return math.floor(num * mult + 0.5) / mult
end
