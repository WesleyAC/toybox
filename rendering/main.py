from wireframe import Model
from viewer import Viewer

if __name__ == '__main__':
    cube_nodes = [(50, 50, 50 ),
                  (100,50, 50 ),
                  (50, 100,50 ),
                  (100,100,50 ),
                  (100,50, 100),
                  (50, 100,100),
                  (100,100,100),
                  (100,100,100)]
    cube_edges = [(0,7),
                  (2,5),
                  (1,4),
                  (3,6),
                  (7,4),
                  (5,6),
                  (0,1),
                  (2,3),
                  (0,2),
                  (1,3),
                  (4,6),
                  (5,7)]
    cube = Model(cube_nodes, cube_edges)
    viewer = Viewer([cube])
    viewer.run()
