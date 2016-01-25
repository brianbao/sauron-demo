#!/bin/bash

# The following variables are available to us
# REVISION/SHA/HASH - the git hash we are running on
# REPOSITORY - the ssh path for the repo we are cloning, e.g. git@github.com:zenefits/yourPeople2.git
# COUNT - the number of build nodes that were requested for this run
# INDEX - the index of this build node
# EXTRA - arbitrary string, whatever requester passed into the CI argument

echo 'yay, this test always succeeds'
