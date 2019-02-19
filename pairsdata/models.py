from django.db import models


class WatchlistModel(models.Model):

    id = models.AutoField(primary_key=True)
    ticker_1 = models.CharField(max_length=30, default=None, null=True, blank=True)
    ticker_2 = models.CharField(max_length=30, default=None, null=True, blank=True)
    timestamp = models.CharField(max_length=50, null=True)

    class Meta():
        db_table = 'watchlist'

    def __unicode__(self):
        return '%s %s %s %s' % (
            self.id,
            self.ticker_1,
            self.ticker_2,
            self.timestamp,
            )

