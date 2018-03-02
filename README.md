# Installation
## Using Pip
```terminal
$ pip install git+https://github.com/qiugits/twpy
```

## Prepare Tokens
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


# Usage
**Show help**
```
$ twpy -h
```

**Show your Timeline**
```
$ twpy
```

**Tweet! with example (meme)**
```
$ twpy 'Twitter Addiction!'
$ twpy 'Ahh the class is so boring'
$ twpy 'Sh*t! The professor found me tweeting! F*ck my life!'
$ twpy 'Professor N*sh*'s class is freaking AWESOME!!!'
```

[meme reference](https://twitter.com/YasuharuNishi/status/958213927053099008)

Happy twitter life!


[Twitter Developer]: https://developer.twitter.com

