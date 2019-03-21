# bren-stars
## Definition
This is module to create bren-stars. bren-stars were a creation while taking notes on dot matrix paper (I may have 
been a little distracted).  That is how the square conformation of the star came to be.  Constructing square stars add 
interesting constraints over traditional circle stars. To start, the traditional way to to create stars is to connect 
every other point around the circle until all points are connected.  This however is not as nice in a square 
conformation as many point lie on the same line. Now we're getting to the point where I need to introduce a few numbers.
The first number is the size of the square. The best way that I found to quantify this is by side length which I call _n_.
_n_ accounts for the number of points on each side minus one. The square will have _4n_ points in its perimeter.

I formalized the definition as follows (but am open to a better description):

> A bren-star of order _n_ is a set of _4n_ points arranged in a square where each point is connected to the points _m_ 
  points away (where _m_ is the smallest number that satisfies: _m_ > _n_ and  _m_ is co-prime with _4n_)

## Example bren-stars
![bren-stars](brenstars1-10.png?raw=true "brenstars 1 thru 10")


## Observations
### _m(n)_
One interesting observation is looking at _m_ as a function of _n_:

| _n_   | _m_   |
|:-----:|:-----:|
| 1     | 3     |
| 2     | 3     |
| 3     | 5     |
| 4     | 5     |
| 5     | 7     |
| 6     | 7     |
| ...   | ...   |

_m_ is equal to either _n+1_ or _n+2_. More specifically it is the next largest odd number greater than _n_.

### Interior Points
As this was originally created on dot paper noticed interesting behaviors in the points (having integer 
coordinates) contained by the the stars. Originally I was interested in which points lie inside the inner most shape 
created by the star.  Since then I have identified 2 classes of points:
 + Points on the star: these are any points on one of the lines they include
   - Vertex points - points lying on the perimeter of the square that are used in the construction of the star
   - Intersection points - points where multiple lines intersect
   - Other points on the star
 + Points in the star:  These are points that do not lie on any of the lines and include:
   - Interior - the points that are contained in the central most contiguous area
   - Peripheral - the poins inside the star but not inside the central most shape
