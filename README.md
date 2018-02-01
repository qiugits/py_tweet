# Installation
### Tokens
Please prepare tokens by yourself. 
You can get them from [Twitter Developer][Twitter Developer].
Then store them as environmental values.

**Esample**:\
bash, zsh
```bash
export TWITTER_CONSUMER_KEY='xxxxxxxxxxxxxxxxxxxxxxxxx'
export TWITTER_CONSUMER_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
export TWITTER_ACCESS_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
export TWITTER_ACCESS_TOKEN_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

fish
```fish
set -x TWITTER_CONSUMER_KEY 'xxxxxxxxxxxxxxxxxxxxxxxxx'
set -x TWITTER_CONSUMER_SECRET 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
set -x TWITTER_ACCESS_TOKEN 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
set -x TWITTER_ACCESS_TOKEN_SECRET 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

### Path
Place twpy to anywhere path is set up, or set up path to twpy.

**Esample**:
```terminal
$ cd ~
$ git clone https://github.com/qiugits/py_tweet
$ ln py_tweet/twpy.py $YOUR_PATH/twpy
```

# Usage
```
$ twpy -h
$ twpy
$ twpy 'Twitter Addiction!'
$ twpy 'Ahh the class is so boring'
$ twpy 'Sh*t! The professor found me tweeting! F*ck my life!'
$ twpy 'Professor N*sh*'s class is freaking AWESOME!!!'
```

[reference](https://twitter.com/YasuharuNishi/status/958213927053099008)

Happy twitter life!


[Twitter Developer]: https://developer.twitter.com

