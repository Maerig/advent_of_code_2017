import re
from collections import defaultdict

from day20.particle import Particle
from utils.progress import show_progress
from utils.vector import Vector


ITERATION_COUNT = 10_000
PARTICLE_REGEX = re.compile('p=<(.*)>, v=<(.*)>, a=<(.*)>')


def read_input():
    return [
        Particle(*[
            Vector(*(
                int(n)
                for n in group.split(',')
            ))
            for group in PARTICLE_REGEX.search(line).groups()
        ])
        for line in open('input.txt')
    ]


def part_1(particles):
    for i in range(ITERATION_COUNT):
        show_progress(i / ITERATION_COUNT)
        for particle in particles:
            particle.iterate()
    show_progress(1)

    return min(
        ((i, p) for i, p in enumerate(particles)),
        key=lambda pair: (pair[1].position.manhattan_distance())
    )[0]


def part_2(particles):
    for i in range(ITERATION_COUNT):
        show_progress(i / ITERATION_COUNT)

        positions = defaultdict(list)
        for particle in particles:
            particle.iterate()
            positions[particle.position].append(particle)

        for group in positions.values():
            if len(group) > 1:
                # Collision
                for particle in group:
                    particles.remove(particle)
    show_progress(1)

    return len(particles)


if __name__ == '__main__':
    print(f"\nPart 1: {part_1(read_input())}")
    print(f"\nPart 2: {part_2(read_input())}")
