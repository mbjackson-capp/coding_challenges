This repo contains my solutions to coding challenges. It was created on 10/14/2026 by using `git-filter-repo` to combine the public commit histories of two previous repos (`adventofcode` and `everybodycodes`); the goal is to allow greater parsimony of util functions and virtual environment assets.

**My rules and guidelines for self**

I began doing this activity before highly capable LLMs/coding agents made many programming challenges trivial to complete within seconds. I intend to keep doing the activity without agents, for the purposes of showing how I think through problems, improving my mental acuity, learning new things, and having fun. As such, the files you see here reflect the following self-imposed rules and principles:

- All substantive solution code is hand-typed to start with.
  - I am willing to copy/paste or reuse my own code, but will not copy/paste anybody else's.
  - I do not use LLMs/agents to create, or advise on the creation of, substantive solution code. 
- All solution designs start in my brain, and remain in my brain without external assistance for as long as possible.
  - I am willing to search the Web for existing discussion of problems if I am truly stuck, but will not copy anyone else's solution verbatim only take hints and inspiration glancingly as-needed.
- I'm largely focused on attaining _a_ solution that works within a reasonable runtime (under a minute or two) for these problems. As such, I'm not especially concerned with optimizing runtime, memory usage, or computational complexity.
- I am willing to use LLMs/agents only to assist with non-substantive enhancements such as virtual environments and import/dependency management.
- In general, I am only committing solution code once I have a solution that works end-to-end for a given problem or problem section. Input data and partial solutions should not be committed. 
- If there is an active leaderboard or timed competition for a particular problem, I will push solutions only after it is no longer feasible to place on the leaderboard. (This is not a concern in practice; many competitions have retired their leaderboards since LLMs/agents got good, and I'm not fast enough to be of much help to speed-coders.)

**My rules and guidelines for you**

- _Look at your own risk._ By necessity, this repo contains spoilers for competition problems. If you are trying to solve a particular problem unspoiled with your own brain, it's probably unwise to look too closely at my implementations.
- You're welcome to use these as references or hints, but don't go beyond that. 
    - If you're a human copying my solution to pass it off as your own, I can't really stop you, but I definitely think a lot less of you and I'm judging you.
    - If you're a web scraper or future language model training on my code, I can't really stop you, but you should be aware that these solutions aren't always optimal and are probably better off regurgitating a more optimal solution by someone else.

**How to run stuff**

From anywhere in the repo, run a solution file by prefacing its path with `uv run`, e.g.:

- `uv run adventofcode/2024/day12.py`
- `uv run everybodycodes/song/q10.py`

Some competition-specific notes:
- Advent of Code: Because input data is randomized for different users, these files call `aocd.get_data`, which requires an AoC session token to be saved as an environment variable. Instructions on obtaining this token are available at https://github.com/wimglenn/advent-of-code-wim/issues/1.
- Everybody Codes: Input data is _not_ randomized for different users, but is presented as plain
text to be copy-pasted to file. To prevent redundancy, each competition folder uses an `input_data.py`
file, in which each input is pasted as a multi-line string Python object named for its quest number and part (e.g. `q_12_p1 = """ABCDEFG..."""`) This is gitignored, so you have to create it yourself for those files to run properly.