// electron simulator
ParticleSystem ps;
float radius = 100;
int electrons = 64;
float threshold;
PGraphics buf;

void setup() {
  size(1080, 720, P3D);
  background(0);

  buf = createGraphics(720,720, P3D);



  //generate electrons
  ArrayList<Particle> particles = new ArrayList<Particle>();
  for( int i=0; i < electrons; i++ ){
    particles.add(new Electron(
      PVector.mult(PVector.random3D(),radius * 1.1),
      PVector.mult(PVector.random3D(),radius/100)
    ));
  }

  ps = new ParabolicParticleSystem(particles);

  textFont(createFont("Arial",12,false));
}

void draw() {
  //pause drawing if mouse pressed
  if (!mousePressed) return;
  ps.update();

  //draw buffer
  buf.beginDraw();

  //fade last frame
  buf.camera();
  buf.fill(0,0,0,10);
  buf.rect(0,0,buf.width, buf.height);

  //display lines on buffer
  buf.camera(
    0,0,radius * 3,
    0,0,0,
    0,1,0
  );

  threshold = radius * 2 / pow(ps.count, 0.5);
  for(int i = 0; i < ps.count; i++){
    for(int j = i+1; j < ps.count; j++){
      float d = ps.distances[i][j];
      if(d < threshold){
        Particle p = ps.particles.get(i);
        Particle q = ps.particles.get(j);
        buf.stroke(255,255,255,127);
        buf.line(p.x.x, p.x.y, p.x.z, q.x.x, q.x.y, q.x.z);
      }
    }
  }

  //display balls on buffer
  for( Particle p : ps.particles ){
    buf.pushMatrix();
    buf.translate(p.x.x, p.x.y, p.x.z);
    buf.noStroke();
    buf.fill(p.c);
    buf.sphere(p.r);
    buf.popMatrix();

  }
  buf.endDraw();

  //write to window
  //clear window
  background(0);

  //write buffer to window
  image(buf, 0, 0);


  //write text window
  text(ps.toString(), buf.width, 0, width - buf.width, height);


  //update particle system
  ps.update();
  ps.step();

}

class Particle {
  PVector x; //position
  PVector v; //velocity
  float m;   //mass
  float q;   //charge
  float r;   //radius
  color c;   //colour

  Particle(PVector x, PVector v, float m, float q, float r, color c){
    this.x = x;
    this.v = v;
    this.m = m;
    this.q = q;
    this.r = r;
    this.c = c;
  }

  void update(PVector f){ //sum of forces
    PVector a = PVector.div(f,m);
    v.add(a);
    PVector.mult( PVector.add(x,v), .999, x);
  }

  String toString(){
    return x.toString();
  }
}

class Electron extends Particle{
  Electron(PVector x, PVector v){
    super(x, v, 1, -10, 1, color(255, 255, 0));
  }
}

class Proton extends Particle{
  Proton(PVector x, PVector v){
    super(x, v, 100, 1, 1, color(255, 0, 0));
  }
}

import java.util.ListIterator;

class ParticleSystem {
  ArrayList<Particle> particles;
  int count;
  float[][] distances;
  PVector[] forces;

  ParticleSystem( ArrayList<Particle> particles ){
    count = 0;
    this.particles = particles;
    update();
  }

  ParticleSystem(){
    this( new ArrayList<Particle>() );
  }

  void update(){
    if( count != particles.size() ){
      count = particles.size();
      forces = new PVector[count];
      distances = new float[count][count];
    }

    //reset forces
    for(int i = 0; i < count; i++){
      forces[i] = f_home(particles.get(i));
    }

    for(int i = 0; i < count; i++){
      for(int j = i+1; j < count; j++){
        Particle p = particles.get(i);
        Particle q = particles.get(j);
        PVector d = PVector.sub(q.x, p.x);
        distances[i][j] = d.mag();
        d.setMag(- p.q * q.q / d.magSq() );
        PVector.add(forces[i], d, forces[i]);
        PVector.sub(forces[j], d, forces[j]);
      }
    }
  }

  void step(){
    assert( distances != null && forces != null );
    ListIterator<Particle> litr = particles.listIterator();
    while(litr.hasNext()){
      int i = litr.nextIndex();
      litr.next().update(forces[i]);
    }
  }

  PVector f_home( Particle p ){
    return new PVector();
  }

  String toString(){
    String[] coordinates = new String[particles.size()];
    for(int i=0; i<particles.size(); i++){
      Particle P = particles.get(i);
      coordinates[i] = P.toString();
    }
    return join(coordinates, "\n");
  }
}

class ParabolicParticleSystem extends ParticleSystem{
  ParabolicParticleSystem( ArrayList<Particle> particles ){
    super( particles );
  }

  PVector f_home( Particle p ){
    PVector f = p.x.get();
    f.setMag(-p.x.mag()/100);
    return f;
  }
}
