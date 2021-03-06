# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Indicator'
        db.create_table(u'django_worldbank_indicator', (
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45, primary_key=True)),
            ('sourceOrganization', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.Source'])),
            ('sourceNote', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['Indicator'])

        # Adding M2M table for field topics on 'Indicator'
        m2m_table_name = db.shorten_name(u'django_worldbank_indicator_topics')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('indicator', models.ForeignKey(orm[u'django_worldbank.indicator'], null=False)),
            ('topic', models.ForeignKey(orm[u'django_worldbank.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['indicator_id', 'topic_id'])

        # Adding model 'Country'
        db.create_table(u'django_worldbank_country', (
            ('capitalCity', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('incomeLevel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.IncomeLevel'])),
            ('adminregion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.Adminregion'])),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5, primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.Region'])),
            ('lendingType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.LendingType'])),
        ))
        db.send_create_signal(u'django_worldbank', ['Country'])

        # Adding model 'Region'
        db.create_table(u'django_worldbank_region', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=90, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5, primary_key=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['Region'])

        # Adding model 'Adminregion'
        db.create_table(u'django_worldbank_adminregion', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=90, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5, primary_key=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['Adminregion'])

        # Adding model 'Topic'
        db.create_table(u'django_worldbank_topic', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=65, null=True, blank=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['Topic'])

        # Adding model 'Source'
        db.create_table(u'django_worldbank_source', (
            ('id', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['Source'])

        # Adding model 'IndicatorData'
        db.create_table(u'django_worldbank_indicatordata', (
            ('indicator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.Indicator'])),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_worldbank.Country'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5, primary_key=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['IndicatorData'])

        # Adding model 'IncomeLevel'
        db.create_table(u'django_worldbank_incomelevel', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5, primary_key=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['IncomeLevel'])

        # Adding model 'LendingType'
        db.create_table(u'django_worldbank_lendingtype', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5, primary_key=True)),
        ))
        db.send_create_signal(u'django_worldbank', ['LendingType'])


    def backwards(self, orm):
        # Deleting model 'Indicator'
        db.delete_table(u'django_worldbank_indicator')

        # Removing M2M table for field topics on 'Indicator'
        db.delete_table(db.shorten_name(u'django_worldbank_indicator_topics'))

        # Deleting model 'Country'
        db.delete_table(u'django_worldbank_country')

        # Deleting model 'Region'
        db.delete_table(u'django_worldbank_region')

        # Deleting model 'Adminregion'
        db.delete_table(u'django_worldbank_adminregion')

        # Deleting model 'Topic'
        db.delete_table(u'django_worldbank_topic')

        # Deleting model 'Source'
        db.delete_table(u'django_worldbank_source')

        # Deleting model 'IndicatorData'
        db.delete_table(u'django_worldbank_indicatordata')

        # Deleting model 'IncomeLevel'
        db.delete_table(u'django_worldbank_incomelevel')

        # Deleting model 'LendingType'
        db.delete_table(u'django_worldbank_lendingtype')


    models = {
        u'django_worldbank.adminregion': {
            'Meta': {'object_name': 'Adminregion'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'})
        },
        u'django_worldbank.country': {
            'Meta': {'object_name': 'Country'},
            'adminregion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.Adminregion']"}),
            'capitalCity': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5', 'primary_key': 'True'}),
            'incomeLevel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.IncomeLevel']"}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lendingType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.LendingType']"}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.Region']"})
        },
        u'django_worldbank.incomelevel': {
            'Meta': {'object_name': 'IncomeLevel'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'django_worldbank.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.Source']"}),
            'sourceNote': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sourceOrganization': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['django_worldbank.Topic']", 'symmetrical': 'False'})
        },
        u'django_worldbank.indicatordata': {
            'Meta': {'object_name': 'IndicatorData'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.Country']"}),
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5', 'primary_key': 'True'}),
            'indicator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_worldbank.Indicator']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'django_worldbank.lendingtype': {
            'Meta': {'object_name': 'LendingType'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'django_worldbank.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '90', 'null': 'True', 'blank': 'True'})
        },
        u'django_worldbank.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'django_worldbank.topic': {
            'Meta': {'object_name': 'Topic'},
            'id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['django_worldbank']