from .api import Twitter
import click

__version__ = '1.0'


@click.command()
@click.argument('tweet', required=False)
@click.version_option(version=__version__)
@click.help_option('-h', '--help')
def run_command(tweet):
    '''This command helps you tweet
    or watch timeline from commandline.

    \b
    To post a Tweet, just hand a string to [TWEET].
    Example:
      $ twpy "my first tweet from command line!"

    \b
    To watch the Timeline, give no options but just command twpy.
    Example:
      $ twpy
    '''
    if tweet:
        # post a tweet.
        text = tweet
        Twitter().post_tweet(text)
    else:
        # get timeline.
        Twitter().get_timeline()


def main():
    run_command()
