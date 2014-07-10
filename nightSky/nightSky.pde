// http://patakk.tumblr.com/nightSky
ArrayList<Point> points = new ArrayList<Point>();
ArrayList<Line> lines = new ArrayList<Line>();
int N = 500;
float time = 0;
float dst;
float lim = 125;

void setup() {
  size(700, 300);
  smooth();
  N = int(500.0 * dist(0, 0, width/2, height/2)/dist(0, 0, 1920/2, 1080/2));
  lim = 160.0 * dist(0, 0, width/2, height/2)/dist(0, 0, 1920/2, 1080/2);
  background(0);
  int n = 0;
  //noiseSeed(5);
  //randomSeed(1200);
  while (n < N) {
    float x, y, rx, ry, a;
    rx = random(width/2 * 0.74) + random(40);
    ry = random(height/2 * 0.84) + random(40);
    a = random(2*PI);
    x = rx * cos(a);
    y = ry * sin(a);
    float dx = map(x, 0, width/2, 0, 1.15);
    float dy = map(y, 0, height/2, 0, 1.35);
    float prob = pow(2.72, -(dx*dx*2 + dy*dy*2));
    if (random(1) < prob) {
      points.add(new Point(x, y));
      n++;
    }
  }

  for (n = 0; n < N-1; n++) {
    float x1 = points.get(n).cx;
    float y1 = points.get(n).cy;
    for (int m = n+1; m < N; m++) {
      float x2 = points.get(m).cx;
      float y2 = points.get(m).cy;
      if (dist(x1, y1, x2, y2) < lim/3) {
        lines.add(new Line(n, m));
      }
    }
  }

  strokeWeight(0.8);
}

void draw() {
  background(0);
  translate(width/2, height/2);

  for (int n = 0; n < N; n++) {
    points.get(n).update();
    points.get(n).display();
  }

  for (int n = 0; n < lines.size(); n++) {
    float x1 = points.get(lines.get(n).j).x;
    float y1 =  points.get(lines.get(n).j).y;
    float x2 = points.get(lines.get(n).k).x;
    float y2 =  points.get(lines.get(n).k).y;
    float amp = map(dist((x1+x2)/2, (y1+y2)/2, 0, 0), 0, dist(width/2, height/2, 0, 0), 2, 8);
    dst = map(noise((x1+x2)/2 * 0.03, (y1+y2)/2 * 0.03), 0, 1, 5, lim/2);
    if (dist((x1+x2)/2, (y1+y2)/2, mouseX - width/2, mouseY - height/2) < lim)
      dst = dst * map(dist((x1+x2)/2, (y1+y2)/2, mouseX - width/2, mouseY - height/2), 0, lim, amp, 1);
    if (dist(x1, y1, x2, y2) < dst) {
      float strk = map(dist(x1, y1, x2, y2), 0, dst, 85, 0);
      stroke(255, strk);
      line(x1, y1, x2, y2);
    }
  }

  time = time + 1;
}

class Line {
  int j, k;
  Line(int jin, int kin) {
    j = jin;
    k = kin;
  }
}

class Point {
  float cx, cy, r, d;
  boolean rt;
  float ph;
  float x, y;

  Point(float xin, float yin) {
    cx = xin;
    cy = yin;
    r = random(5, 30);
    d = map(r, 5, 30, 0.5, 2);
    if (random(1) > 0.5)
      rt = true;
    else
      rt = false;
    ph = random(360);
  }

  void update() {
    if (rt)
      x = cx + r * cos(radians(time * d + ph));
    else
      x = cx + r * cos(radians(-time * d + ph));
    if (rt)
      y = cy + r * sin(radians(time * d + ph));
    else
      y = cy + r * sin(radians(-time * d + ph));
  }

  void display() {
    noStroke();
    fill(255);
    ellipse(x, y, d, d);
  }
}
