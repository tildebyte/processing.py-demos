float time = 0;
int radius = 200;
int ellipseRadius = 2;
float timeStep = 0.01;


void setup(){
    size(512, 512, P3D);
    rectMode(RADIUS);
    ellipseMode(RADIUS);
    // background(0);
}

void draw(){
    translate(256, 256, 0);
    rotateX(TAU / 2);
    with pushMatrix():
        fill(0, 10);
        noStroke();
        translate(-width, width, -500);
        rect(0, 0, width * 2, height * 2);
    time += timeStep;
    float lon = cos(time + sin(time * 0.31)) * 2 + sin(time * 0.83) * 3 + time * 0.02;
    float lat = sin(time * 0.7 + 1) - cos(3 + time * 0.43 + sin(time) * 0.13) * 2.3;
    float x = radius * sin(lat) * cos(lon);
    float y = radius * sin(lat) * sin(lon);
    float z = radius * cos(lat);
    // point(x, y, z);
    fill(250, 50);
    stroke(190, 25);
    translate(0, 0, z);
    ellipse(x, y, ellipseRadius, ellipseRadius);
}
