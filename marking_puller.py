# -*- coding: UTF-8 -*-
"""Get the latest copy of all the repos.

This pulls the latest copy of all the repos
It can clone new repos if you set THERE_ARE_NEW_STUDENTS to true
"""

from __future__ import division
from __future__ import print_function
import git
import os
import pandas as pd
import requests
from StringIO import StringIO

# from week1.tests import theTests as w1test
from importlib import import_module
WEEK_NUMBER = 1
w1test = import_module("week{}.tests".format(WEEK_NUMBER), "theTests")
w1test = w1test.theTests

LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
print("LOCAL", LOCAL)
print("CWD", CWD)

rootdir = '../code1161StudentRepos'
THERE_ARE_NEW_STUDENTS = True


def getDFfromCSVURL(url, columnNames=False):
    """Get a csv of values from google docs."""
    r = requests.get(url)
    data = r.content
    if columnNames:
        return pd.read_csv(StringIO(data), header=0, names=columnNames)
    else:
        return pd.read_csv(StringIO(data))


def update_for_new_students():
    """Get an updated copy of the spreadsheet."""
    ss_of_details_url = ("https://docs.google.com/spreadsheets/d/"
                         "1lpgfIo4A7mMpvo66w0tOsRMzr-UJHX5Ja-QEZKiR7_Q/"
                         "pub?gid=1619618387&single=true&output=csv")

    student_details = getDFfromCSVURL(ss_of_details_url, ["timestamp",
                                                          "their_name",
                                                          "student_number",
                                                          "repo_url"])
    print("student_details:\n", student_details)

    for index, student in student_details.iterrows():
        try:
            git.Repo.clone_from(student.repo_url,
                                os.path.join(rootdir, student.student_number))
            print("new repo for", student.their_name)
        except Exception:
            print("we already have have", student.their_name)


if THERE_ARE_NEW_STUDENTS:
    update_for_new_students()

dirList = os.listdir(rootdir)


def markWk1():
    """Mark week 1's exercises."""
    print("dirList:", dirList)

    for student_repo in dirList:
        git.cmd.Git(os.path.join(rootdir, student_repo)).pull()

    results = []
    for student_repo in dirList:
        print("\nFor:", student_repo)
        marks = w1test(os.path.join(rootdir, student_repo, "week1"))
        marks.update({"student_number": student_repo})
        results.append(marks)

    print("\n\nResults:")
    resultsDF = pd.DataFrame(results)
    print(resultsDF)
    resultsDF.to_csv(os.path.join(CWD, "week{}marks.csv".format(WEEK_NUMBER)))


def csvOfDetails():
    """Make a CSV of all the students."""
    import ruamel.yaml as yaml
    results = []
    for student_repo in dirList:
        try:
            path = os.path.join(rootdir, student_repo, "aboutMe.yml")
            details = open(path).read()
            details = details.replace("@", "^AT^")
            details = details.replace("é", "e")
            details = details.replace(":([^ /])", ": $1")
            details = yaml.load(details, yaml.RoundTripLoader)
            details["repoName"] = student_repo
            details["error"] = False
            results.append(details)
            if details["studentNumber"] == "z1234567":
                print(student_repo, "hasn't updated")
        except Exception as e:
            results.append({'error': e, "repoName": student_repo})

    print("\n\nResults:")
    resultsDF = pd.DataFrame(results)
    # print(resultsDF)
    resultsDF.to_csv(os.path.join(CWD,
                                  "studentDetails.csv".format(WEEK_NUMBER)))

csvOfDetails()
