/*
  1. One hundred `HRect`
  2. Of randomly-selected size
  3. Each having semi-tranparent fill and stroke
  4. Each colored according to an underlying `HColorField`
  5. Each rotating around its own center at a randomly-selected speed and
     direction
  6. Randomly distributed around the circumference of
  7. One of several concentric circles
  8. All rotating at a randomly-selected speed and direction around a common
     center point

  Implementation by Ben Alkov 7-12 August 2014
*/

import hype.core.util.*;
import hype.core.behavior.*;
import hype.core.collection.*;
import hype.core.colorist.*;
import hype.core.drawable.*;
import hype.core.interfaces.*;
import hype.core.layout.*;
import hype.extended.behavior.*;
import hype.extended.colorist.*;
import hype.extended.drawable.*;
import hype.extended.layout.*;
import hype.extended.util.*;


HColorField colors;
int centerX;
int centerY;
HDrawablePool visiblePool;
HDrawablePool parentPool;


void setup() {
    size(800, 800);
    centerX = width / 2;
    centerY = height / 2;
    H.init(this).background(#595E6E);
    smooth();
    colors = new HColorField(width, height)
              .addPoint(0, centerY, #082891, 0.7)
              .addPoint(width, centerY, #529108, 0.7)
              .fillAndStroke();
    // No `requestAll()` for the visible HRects. They will be requested inside
    // the `parentPool` callback.
    visiblePool = new HDrawablePool(100)
                      .add(new HRect())
                      .onCreate(
                        new HCallback() {
                          public void run(Object obj) {
                            int radius;
                            HRect drawable = (HRect) obj;
                            // Position this HRect at a random position on an orbit randomly chosen
                            // from a set of four.
                            float angle = random(TAU);
                            // `randint` slightly offsets the position so we don't end up with the
                            // visible HRects orbiting on *exact* circles.
                            float chance = random(1);
                            if (chance < 0.18) {
                                radius = 100 + (int)(Math.random() * 35);
                            } else if (chance < 0.50) {
                                radius = 200 + (int)(Math.random() * 35);
                            } else if (chance < 0.78) {
                                radius = 325 + (int)(Math.random() * 35);
                            } else {
                                radius = 450 + (int)(Math.random() * 35);
                            }
                            float createX = centerX + (cos(angle) * radius);  // `angle` *must* be radians.
                            float createY = centerY + (sin(angle) * radius);  //
                            drawable.strokeWeight(2)
                                    .stroke(#000000, 196)
                                    .fill(#000000, 100)
                                    .size(random(35, 60))
                                    // .rounding(2.0)
                                    .rotation(random(360))
                                    .loc(createX, createY)
                                    .anchorAt(H.CENTER);
                            colors.applyColor(drawable);
                            // Apply a rotation with random speed and direction. This causes
                            // the HRect to rotate around *its* center.
                            float speed = avoidZero(4.0, 0.5);
                            new HRotate(drawable, speed);
                          }
                        }
                      );
    parentPool = new HDrawablePool(100)
                  .autoAddToStage()
                  .add(new HRect())
                  .onCreate(
                    new HCallback() {
                      public void run(Object obj) {
                        HRect parent = (HRect) obj;
                        // Pull one HRect from the pool of visible HRects.
                        HRect child = (HRect) visiblePool.request();
                        parent.noStroke()
                              .noFill()
                              .size(3)
                              .rotation(random(360));
                        // In order for the object to rotate *on* the orbit, around the
                        // *orbit's* center, we have to set its center to the center of the
                        // orbit, and then calculate its position on the orbit based on the
                        // child's position.
                        parent.loc(centerX, centerY)
                              .anchor(abs(child.x() - centerX),
                                      abs(child.y() - centerY));
                        parent.add(child);
                        // Move the child to the parent's center.
                        child.locAt(H.CENTER);
                        float speed = avoidZero(0.5, 0.01);
                        new HRotate(parent, speed);
                      }
                    }
                  )
                  .requestAll();
}

void draw() {
    H.drawStage();
}


// This is specifically used to avoid zero or synchronous rotation. We want all
// visible HRects to *appear* to rotate in place.
float avoidZero(float limit, float tolerance) {
    /*
    Return a random value in the range from -`limit` to `limit` - 1, excluding
    the inner range from -`tolerance` to `tolerance` - 1 (and, logically, zero
    as well).
    */
    float value = random(limit * -1, limit);
    while (tolerance * -1 < value && value < tolerance) {
        value = random(limit * -1, limit);
        continue;
    }
    return value;
}
