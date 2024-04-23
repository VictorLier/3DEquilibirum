import numpy as np

class Force:
    def __init__(self, x_pos, y_pos, z_pos, x_force, y_force, z_force) -> None:
        '''
        x_pos: x position of the force
        y_pos: y position of the force
        z_pos: z position of the force
        x_force: x component of the force, 0 if not given, None if support
        y_force: y component of the force, 0 if not given, None if support
        z_force: z component of the force, 0 if not given, None if support
        '''
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.x_force = x_force
        self.y_force = y_force
        self.z_force = z_force
        self.pos = np.array([x_pos, y_pos, z_pos])
        
        self.force = np.array([x_force, y_force, z_force])
    
    @property
    def magnitude(self):
        '''
        Calculates the magnitude of the force
        '''
        return np.linalg.norm(self.force)
    
    @property
    def normal(self):
        '''
        Calculates the normal of the force vector
        '''
        return self.force / self.magnitude
    
    def update(self, x_pos = False, y_pos = False, z_pos = False, x_force = False, y_force = False, z_force = False):
        if x_pos:
            self.x_pos = x_pos
        if y_pos:
            self.y_pos = y_pos
        if z_pos:
            self.z_pos = z_pos
        if x_force:
            self.x_force = x_force
        if y_force:
            self.y_force = y_force
        if z_force:
            self.z_force = z_force
        self.pos = np.array([self.x_pos, self.y_pos, self.z_pos])
        self.force = np.array([self.x_force, self.y_force, self.z_force])



if __name__ == '__main__':
    f = Force(0, 0, 0, 1, 1, 1)
    print(f.magnitude)
    print(f.normal)
    f.update(x_force = 2)
    print(f.magnitude)
    print(f.normal)
    f.update(y_force = 3)
    print(f.magnitude)
    print(f.normal)
    f.update(z_force = 4)
    print(f.magnitude)
    print(f.normal)