# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recipe'
        db.create_table(u'public_recipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cook_time', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cook_method', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_ingredients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm[u'public.ingredient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'ingredient_id'])

        # Adding model 'Ingredient'
        db.create_table(u'public_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('glycemic_index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'public', ['Ingredient'])


    def backwards(self, orm):
        # Deleting model 'Recipe'
        db.delete_table(u'public_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_ingredients'))

        # Deleting model 'Ingredient'
        db.delete_table(u'public_ingredient')


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
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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