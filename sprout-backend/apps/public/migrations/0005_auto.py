# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field tag on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_tag'))

        # Adding M2M table for field tags on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('tag', models.ForeignKey(orm[u'public.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'tag_id'])


    def backwards(self, orm):
        # Adding M2M table for field tag on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('tag', models.ForeignKey(orm[u'public.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'tag_id'])

        # Removing M2M table for field tags on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_tags'))


    models = {
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'glycemic_index': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cook_time': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recipe_description': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Tag']", 'symmetrical': 'False'})
        },
        u'public.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['public']