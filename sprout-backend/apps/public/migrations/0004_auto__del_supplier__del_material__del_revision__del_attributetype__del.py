# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Supplier'
        db.delete_table(u'public_supplier')

        # Deleting model 'Material'
        db.delete_table(u'public_material')

        # Deleting model 'Revision'
        db.delete_table(u'public_revision')

        # Deleting model 'AttributeType'
        db.delete_table(u'public_attributetype')

        # Deleting model 'ItemType'
        db.delete_table(u'public_itemtype')

        # Deleting model 'Color'
        db.delete_table(u'public_color')

        # Deleting model 'Template'
        db.delete_table(u'public_template')

        # Adding model 'Tag'
        db.create_table(u'public_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'public', ['Tag'])

        # Adding M2M table for field tag on 'Recipe'
        m2m_table_name = db.shorten_name(u'public_recipe_tag')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm[u'public.recipe'], null=False)),
            ('tag', models.ForeignKey(orm[u'public.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['recipe_id', 'tag_id'])


        # Changing field 'Ingredient.glycemic_index'
        db.alter_column(u'public_ingredient', 'glycemic_index', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding unique constraint on 'Ingredient', fields ['name']
        db.create_unique(u'public_ingredient', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Ingredient', fields ['name']
        db.delete_unique(u'public_ingredient', ['name'])

        # Adding model 'Supplier'
        db.create_table(u'public_supplier', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Material'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Supplier'])

        # Adding model 'Material'
        db.create_table(u'public_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Material'])

        # Adding model 'Revision'
        db.create_table(u'public_revision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Revision'])

        # Adding model 'AttributeType'
        db.create_table(u'public_attributetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['AttributeType'])

        # Adding model 'ItemType'
        db.create_table(u'public_itemtype', (
            ('abb', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_non_inventory_item', self.gf('django.db.models.fields.BooleanField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_template', self.gf('django.db.models.fields.BooleanField')()),
            ('is_inventory', self.gf('django.db.models.fields.BooleanField')()),
            ('is_recoup', self.gf('django.db.models.fields.BooleanField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['ItemType'])

        # Adding model 'Color'
        db.create_table(u'public_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Color'])

        # Adding model 'Template'
        db.create_table(u'public_template', (
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('item_id', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attribute1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'public', ['Template'])

        # Deleting model 'Tag'
        db.delete_table(u'public_tag')

        # Removing M2M table for field tag on 'Recipe'
        db.delete_table(db.shorten_name(u'public_recipe_tag'))


        # User chose to not deal with backwards NULL issues for 'Ingredient.glycemic_index'
        raise RuntimeError("Cannot reverse this migration. 'Ingredient.glycemic_index' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Ingredient.glycemic_index'
        db.alter_column(u'public_ingredient', 'glycemic_index', self.gf('django.db.models.fields.IntegerField')())

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
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['public.Tag']", 'symmetrical': 'False'})
        },
        u'public.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['public']