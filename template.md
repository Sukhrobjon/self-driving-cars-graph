# Modeling Map Using Graph Theory

- This project will tackle the common problem of modeling maps. When we use maps we always want choose the fastest route or sometimes safest route. The entire premise of Google Maps is using a big giant graph with nodes and edges to figure out fastest or shortest way to travel. That’s all Google Maps is–a big graph with lots of nodes and edges.[resource](https://blogs.cornell.edu/info2040/2011/09/14/google-maps-its-just-one-big-graph/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

Clone the project

```
git clone https://github.com/Sukhrobjon/self-driving-cars-graph.git
```

End with an example of getting some data out of the system or using it for a little demo

## Running on Terminal

```
cd self-driving-cars-graph
```
```python3 run.py Graphs/inputs/maps_data.txt```

### Sample Output

```bash
=========================Visualize the map: Make a graph=========================
Vertices: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
Number of Edges: 9
The Edge List:
('A', 'D', 15)
('A', 'E', 12)
('A', 'F', 72)
('A', 'G', 7)
('G', 'B', 55)
('B', 'C', 12)
('C', 'D', 7)
('D', 'E', 33)
('E', 'F', 11)
=========================Problem One: Fastest Route=========================
Fastest route from A to C is: A->D->C with total distance of 22 miles!
=========================Problem Two: Busiest Intersection=========================
A connected 4 of intersections.
=========================Problem Three: Find near me=========================
These locations are 25 away from A.
Locations are: C, D, E, F, G
```

## Authors

* **Sukhrob Golibboev** - *Initial work* - [Modeling Maps](https://github.com/PurpleBooth)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


