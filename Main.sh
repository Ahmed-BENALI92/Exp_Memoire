#!/bin/bash

function initSearchGit()
{
    curl "https://api.github.com/search/repositories?q=src+in:app+language:js">Test.json
}
initSearchGit
exit