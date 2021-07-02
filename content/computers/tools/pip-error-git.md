Title: Correct pip error when installing or freezing with git repos
Slug: correct-pip-error-installing-freezing-with-git-repos
Date: 2021-04-09
Author: Marc-Olivier Titeux
Email: marcolivier.titeux@gmail.com
Summary: Do not let colors in your way of the pip

I kept having the following issue when using pip freeze with a git repos:

    Complete output from command /usr/local/bin/git rev-parse origin/HEAD:
    fatal: ambiguous argument 'origin/HEAD': unknown revision or path not in the working tree.

    Use '--' to separate paths from revisions, like this:

    'git <command> [<revision>...] -- [<file>...]'

    origin/HEAD

    ----------------------------------------
    Error when trying to get requirement for VCS system Command /usr/local/bin/git rev-parse origin/HEAD failed with error code 128 in /home/mtiteux/.virtualenvs/myproject, falling back to uneditable format
    Could not determine repository location of /home/mtiteux/.virtualenvs/myproject
    
This drove me quite perplexed as to the reason why I could not correctly parsed `requirements.txt` files and got a when using `pip freeze`:
    ## !! Could not determine repository location

Then, I stumbled upon on [this blog](http://koyekola.tumblr.com/post/7193469590/pip-error-installing-from-git-branch-tag-fixed) (link broken) post which explained everything. The solution proposed (edit .gitconfig [color]) solved the issue!

As a reference, in case of the link goes down, I am copy&pasting the clue here:

The cause is the .gitconfig’s color setting:

    [color]
            ui = always
Replace it by

    [color]
            ui = auto

