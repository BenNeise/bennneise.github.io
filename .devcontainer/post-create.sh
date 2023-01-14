#!/bin/sh

rm Gemfile.lock

# Install the version of Bundler.
if [ -f Gemfile.lock ] && grep "BUNDLED WITH" Gemfile.lock > /dev/null; then
    cat Gemfile.lock | tail -n 2 | grep -C2 "BUNDLED WITH" | tail -n 1 | xargs gem install bundler -v
fi

git config --global user.email "ben@neise.co.uk"
git config --global user.name "Ben Neise"
git config --global --add safe.directory $(pwd)

# If there's a Gemfile, then run `bundle install`
# It's assumed that the Gemfile will install Jekyll too
if [ -f Gemfile ]; then
    sudo chown -R $(whoami):$(whoami) /usr/local/rvm/gems/default
    bundle install
fi

