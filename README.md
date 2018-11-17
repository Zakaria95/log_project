Web Development Full Stack Nano Degree
======================================

This is the First project Log Analysis – Done by Zakria kharsa
--------------------------------------------------------------

This Code function
------------------

This code wrote to retrieve log data from data base(news_db), using PSQL, the
code should find the following:

1.  Most popular three articles of all time

2.  Most popular articles’ authors of all time

3.  The day where more than 1% of request lead to error.

Requirement to run this code:
-----------------------------

**Software:**

User terminal like Git Bash or another terminal

Python 3.7 or above

Any python IDE, as Atom or VScode

Vagrant 2.2.1

Virtual box

**Libraries:**

Psycopg

PostgreSQL

Note, if you are going to use FSND_VM, these libraries already installed in the
VM.

Lets get Started:
-----------------

1.  Download the Git bash if you are windows user, if you are Linux or Mac user
    no need

2.  Download Python 3.7 or above

3.  Download and install the Vagrant 2.2.1 based on your OS (
    <https://releases.hashicorp.com/vagrant/2.2.1/>)

4.  Open the git and start the below commands in step 5

5.  Download or Clone the FSND VM, which contain ready environment for this
    project requirement

    Download it then place it where you want,
    (<https://github.com/udacity/fullstack-nanodegree-vm>)

    \$ git clone https://github.com/udacity/fullstack-nanodegree-vm.git FSND_VM

    \$ cd FSND_VM

    \$ cd vagrant

    \$ vagrant up

    Note that the path might change based on the download location

6.  Download the data base file, then unzip it (you can do it through command or
    through and unzip software)

    Link: <https://github.com/mtawil/logs-analysis/files/2498083/newsdata.zip>

Run the vagrant:
----------------

1.  To access the vagrant you should ensure that you are located in vagrant
    directory

    To check type

    \$ pwd

    And you should see that the line start with vagrant like

    \$ ………/vagrant

2.  Start the vagrant access by:

    \$ vagrant ssh

3.  Clone this repo, and ensure to define the shared file of vagrant to be
    cloned to the shred folder of vagrant

    \$ git clone <https://github.com/Zakaria95/log_project.git> vagrant/log
    project

4.  Copy the unzipped db news.sql to the log project folder

5.  Import the data base to the vagrant using the below command

    \$ psql -d news -f newsdata.sql

    This will be done once, then it will stay in the vagrant files.

Running the code:
-----------------

1.  Locat to the log project folder using vagrant, and ensure that the vagrant
    is up

2.  Type

    \$ python log_Pr_zak.py

    Now you should see the following output

    ![](media/c6a289bc987901bafdda6b94bca4ceac.png)

Coding standards:
-----------------

This code been wrote, following the [PEP8 style
guide](https://www.python.org/dev/peps/pep-0008/) , to ensure best coding styles
practices
