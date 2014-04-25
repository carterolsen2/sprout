# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'public_item')

        # Adding field 'Recipe.recipe_description'
        db.add_column(u'public_recipe', 'recipe_description',
                      self.gf('django.db.models.fields.TextField')(default='This is the description'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'public_item', (
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Item'])

        # Deleting field 'Recipe.recipe_description'
        db.delete_column(u'public_recipe', 'recipe_description')


    models = {
        u'public.attributetype': {
            'Meta': {'object_name': 'AttributeType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'glycemic_index': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'abb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_inventory': ('django.db.models.fields.BooleanField', [], {}),
            'is_non_inventory_item': ('django.db.models.fields.BooleanField', [], {}),
            'is_recoup': ('django.db.models.fields.BooleanField', [], {}),
            'is_template': ('django.db.models.fields.BooleanField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'public.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'cook_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cook_time': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Ingredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'recipe_description': ('django.db.models.fields.TextField', [], {})
        },
        u'public.revision': {
            'Meta': {'object_name': 'Revision'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'public.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Material']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.template': {
            'Meta': {'object_name': 'Template'},
            'attribute1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'attribute2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_id': ('django.db.models.fields.IntegerField', [], {}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['public']