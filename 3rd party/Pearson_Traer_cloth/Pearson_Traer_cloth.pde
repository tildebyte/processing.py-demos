import traer.physics.Particle;
import traer.physics.ParticleSystem;
import traer.physics.Vector3D;

float angnoise;
float radiusnoise;
float angle = -1.570796F;
float radius;
ParticleSystem physics;
Particle[][] particles;
int gridSizeX = 125;
int gridSizeY = 75;
int gridMidX;
int gridMidY;
int moverX;
int moverY;

public void setup()
{
  size(500, 300);
  smooth();
  frameRate(24.0F);
  strokeCap(4);
  gridMidX = (int)(gridSizeX / 2);
  gridMidY = (int)(gridSizeY / 2);
  restart();
}

public void restart()
{
  background(255);

  angnoise = random(10.0F);
  radiusnoise = random(10.0F);

  physics = new ParticleSystem(0.0F, 0.01F);

  particles = new Particle[gridSizeY][gridSizeX];

  float f1 = width / gridSizeX;
  float f2 = height / gridSizeY;
  float f3 = f1 / 2.0F;
  moverX = (int)(random(gridSizeX));
  moverY = (int)(random(gridSizeY));
  for (int i = 0; i < gridSizeY; i++) {
    for (int j = 0; j < gridSizeX; j++) {
      particles[i][j] = physics.makeParticle(0.2F, j * f1 + f3, i * f2, 0.0F);
    }
  }
  for (int i = 0; i < gridSizeX; i++) {
    for (int j = 1; j < gridSizeY; j++)
    {
      physics.makeSpring(particles[(j - 1)][i], particles[j][i], 8.0F, 0.5F, f2);
      if (i > 0) {
        physics.makeSpring(particles[j][(i - 1)], particles[j][i], 8.0F, 0.5F, f1);
      }
    }
  }
}

public void clearBackground()
{
  fill(255, 15.0F);
  noStroke();
  rect(0.0F, 0.0F, width, height);
}

public void draw()
{
  physics.tick(0.15F);
  if (frameCount % 100 == 0)
  {
    moverX = (int)(random(gridSizeX));
    moverY = (int)(random(gridSizeY));
  }
  clearBackground();
  stroke(0, 5.0F);

  radiusnoise += 0.02F;
  radius = (noise(radiusnoise) * 400.0F + 100.0F);
  angnoise += 0.01F;
  angle += noise(angnoise) * 10.0F - 5.0F;
  if (angle > 360.0F) {
    angle -= 360.0F;
  }
  if (angle < 0.0F) {
    angle += 360.0F;
  }
  float f1 = radians(angle);
  float f2 = 250.0F + radius * cos(f1);
  float f3 = 150.0F + radius * sin(f1);

  Particle localParticle = particles[moverY][moverX];
  localParticle.position().set(f2, f3, 0.0F);
  localParticle.velocity().set(150.0F, 150.0F, 0.0F);

  noFill();
  for (int i = 0; i < gridSizeY; i++)
  {
    beginShape();
    for (int j = 0; j < gridSizeX; j++) {
      if (particles[i][j] != localParticle) {
        curveVertex(particles[i][j].position().x(), particles[i][j].position().y());
      }
    }
    endShape();
  }
  for (int i = 0; i < gridSizeX; i++)
  {
    beginShape();
    for (int j = 0; j < gridSizeY; j++) {
      if (particles[j][i] != localParticle) {
        curveVertex(particles[j][i].position().x(), particles[j][i].position().y());
      }
    }
    endShape();
  }
}

public void mousePressed()
{
  restart();
}
