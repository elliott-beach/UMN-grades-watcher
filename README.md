I find it annoying that the UMN moodle system doesn't notify you when grades are updated,
so I wrote a script to check grades automatically. Grades are checked every 60 minutes, and, if your grades changed, I send you an email!

## USAGE

To install:

1. Clone the repo.

2. Run `pip install mechanize`.

3. `python checkGrades.py username password [courseIDs] &`

To run the script, enter your x500, password, and the courseIDs of moodle courses you are enrolled in.
Example: `./checkGrades.py beach144 super-secret-password 11026 10430 &`.

You can find the courseID by navigating to the home page for a class. If the url is https://ay16.moodle.umn.edu/course/view.php?id=11026,
then 11026 is the courseID.

## TODO
- [ ] Automate finding courseIDs for courses the student is currently enrolled in.
- [ ] Parse command line arguments intelligently.
- [ ] Upload to Pypi.


## Contributing
You are awesome for contributing!
Raise a Github Issue and tell me about the feature or bugfix you think would be interesting.
