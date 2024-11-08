import os

def run_git_bisect(badhash, goodhash):
    os.system(f"git bisect start {badhash} {goodhash}")
    os.system("git bisect run python manage.py test")

if __name__ == "__main__":
    badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"
    goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
    run_git_bisect(badhash, goodhash)


