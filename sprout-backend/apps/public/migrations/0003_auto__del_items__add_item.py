# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Items'
        db.delete_table(u'public_items')

        # Adding model 'Item'
        db.create_table(u'public_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('item_type_id', self.gf('django.db.models.fields.IntegerField')()),
            ('template_id', self.gf('django.db.models.fields.IntegerField')()),
            ('is_inventory', self.gf('django.db.models.fields.BooleanField')()),
            ('is_figure_cost', self.gf('django.db.models.fields.BooleanField')()),
            ('is_warehouse', self.gf('django.db.models.fields.BooleanField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
            ('is_template', self.gf('django.db.models.fields.BooleanField')()),
            ('is_direct_cost', self.gf('django.db.models.fields.BooleanField')()),
            ('is_update', self.gf('django.db.models.fields.BooleanField')()),
            ('supplier_id', self.gf('django.db.models.fields.IntegerField')()),
            ('mpn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cost', self.gf('django.db.models.fields.IntegerField')()),
            ('purchase_amt', self.gf('django.db.models.fields.IntegerField')()),
            ('purchase_unit_id', self.gf('django.db.models.fields.IntegerField')()),
            ('dens_num', self.gf('django.db.models.fields.IntegerField')()),
            ('dens_num_unit_id', self.gf('django.db.models.fields.IntegerField')()),
            ('dens_den_unit_id', self.gf('django.db.models.fields.IntegerField')()),
            ('drawings', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('attribute_id_1', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_id_2', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_id_3', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_type_id_1', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_type_id_2', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_type_id_3', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('depth', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('revision_id', self.gf('django.db.models.fields.IntegerField')()),
            ('lead_time', self.gf('django.db.models.fields.IntegerField')()),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('moq', self.gf('django.db.models.fields.IntegerField')()),
            ('demand_qrt', self.gf('django.db.models.fields.IntegerField')()),
            ('min_on_hand', self.gf('django.db.models.fields.IntegerField')()),
            ('min_ord_freq', self.gf('django.db.models.fields.IntegerField')()),
            ('demand_dly', self.gf('django.db.models.fields.IntegerField')()),
            ('low_point', self.gf('django.db.models.fields.IntegerField')()),
            ('reorder_point', self.gf('django.db.models.fields.IntegerField')()),
            ('reorder_qty', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_recomb', self.gf('django.db.models.fields.BooleanField')()),
            ('recomb_ratio', self.gf('django.db.models.fields.IntegerField')()),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('inventory_scaler', self.gf('django.db.models.fields.IntegerField')()),
            ('volume', self.gf('django.db.models.fields.IntegerField')()),
            ('transfer_sheet_id', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('critical_features', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'public', ['Item'])


    def backwards(self, orm):
        # Adding model 'Items'
        db.create_table(u'public_items', (
            ('color', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_inventory', self.gf('django.db.models.fields.BooleanField')()),
            ('low_point', self.gf('django.db.models.fields.IntegerField')()),
            ('dens_den_unit_id', self.gf('django.db.models.fields.IntegerField')()),
            ('min_ord_freq', self.gf('django.db.models.fields.IntegerField')()),
            ('inventory_scaler', self.gf('django.db.models.fields.IntegerField')()),
            ('supplier_id', self.gf('django.db.models.fields.IntegerField')()),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('part_no', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('demand_qrt', self.gf('django.db.models.fields.IntegerField')()),
            ('dens_num_unit_id', self.gf('django.db.models.fields.IntegerField')()),
            ('dens_num', self.gf('django.db.models.fields.IntegerField')()),
            ('purchase_unit_id', self.gf('django.db.models.fields.IntegerField')()),
            ('lead_time', self.gf('django.db.models.fields.IntegerField')()),
            ('mpn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('moq', self.gf('django.db.models.fields.IntegerField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
            ('volume', self.gf('django.db.models.fields.IntegerField')()),
            ('demand_dly', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('is_figure_cost', self.gf('django.db.models.fields.BooleanField')()),
            ('reorder_point', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('purchase_amt', self.gf('django.db.models.fields.IntegerField')()),
            ('is_direct_cost', self.gf('django.db.models.fields.BooleanField')()),
            ('is_warehouse', self.gf('django.db.models.fields.BooleanField')()),
            ('is_template', self.gf('django.db.models.fields.BooleanField')()),
            ('attribute_type_id_3', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_type_id_2', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_type_id_1', self.gf('django.db.models.fields.IntegerField')()),
            ('revision_id', self.gf('django.db.models.fields.IntegerField')()),
            ('template_id', self.gf('django.db.models.fields.IntegerField')()),
            ('drawings', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('recomb_ratio', self.gf('django.db.models.fields.IntegerField')()),
            ('cost', self.gf('django.db.models.fields.IntegerField')()),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('transfer_sheet_id', self.gf('django.db.models.fields.IntegerField')()),
            ('min_on_hand', self.gf('django.db.models.fields.IntegerField')()),
            ('critical_features', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('is_update', self.gf('django.db.models.fields.BooleanField')()),
            ('item_type_id', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_id_3', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_id_2', self.gf('django.db.models.fields.IntegerField')()),
            ('attribute_id_1', self.gf('django.db.models.fields.IntegerField')()),
            ('is_recomb', self.gf('django.db.models.fields.BooleanField')()),
            ('reorder_qty', self.gf('django.db.models.fields.IntegerField')()),
            ('depth', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'public', ['Items'])

        # Deleting model 'Item'
        db.delete_table(u'public_item')


    models = {
        u'public.item': {
            'Meta': {'object_name': 'Item'},
            'attribute_id_1': ('django.db.models.fields.IntegerField', [], {}),
            'attribute_id_2': ('django.db.models.fields.IntegerField', [], {}),
            'attribute_id_3': ('django.db.models.fields.IntegerField', [], {}),
            'attribute_type_id_1': ('django.db.models.fields.IntegerField', [], {}),
            'attribute_type_id_2': ('django.db.models.fields.IntegerField', [], {}),
            'attribute_type_id_3': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cost': ('django.db.models.fields.IntegerField', [], {}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {}),
            'critical_features': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'demand_dly': ('django.db.models.fields.IntegerField', [], {}),
            'demand_qrt': ('django.db.models.fields.IntegerField', [], {}),
            'dens_den_unit_id': ('django.db.models.fields.IntegerField', [], {}),
            'dens_num': ('django.db.models.fields.IntegerField', [], {}),
            'dens_num_unit_id': ('django.db.models.fields.IntegerField', [], {}),
            'depth': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'drawings': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory_scaler': ('django.db.models.fields.IntegerField', [], {}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'is_direct_cost': ('django.db.models.fields.BooleanField', [], {}),
            'is_figure_cost': ('django.db.models.fields.BooleanField', [], {}),
            'is_inventory': ('django.db.models.fields.BooleanField', [], {}),
            'is_recomb': ('django.db.models.fields.BooleanField', [], {}),
            'is_template': ('django.db.models.fields.BooleanField', [], {}),
            'is_update': ('django.db.models.fields.BooleanField', [], {}),
            'is_warehouse': ('django.db.models.fields.BooleanField', [], {}),
            'item_type_id': ('django.db.models.fields.IntegerField', [], {}),
            'lead_time': ('django.db.models.fields.IntegerField', [], {}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'low_point': ('django.db.models.fields.IntegerField', [], {}),
            'min_on_hand': ('django.db.models.fields.IntegerField', [], {}),
            'min_ord_freq': ('django.db.models.fields.IntegerField', [], {}),
            'moq': ('django.db.models.fields.IntegerField', [], {}),
            'mpn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part_no': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'purchase_amt': ('django.db.models.fields.IntegerField', [], {}),
            'purchase_unit_id': ('django.db.models.fields.IntegerField', [], {}),
            'recomb_ratio': ('django.db.models.fields.IntegerField', [], {}),
            'reorder_point': ('django.db.models.fields.IntegerField', [], {}),
            'reorder_qty': ('django.db.models.fields.IntegerField', [], {}),
            'revision_id': ('django.db.models.fields.IntegerField', [], {}),
            'supplier_id': ('django.db.models.fields.IntegerField', [], {}),
            'template_id': ('django.db.models.fields.IntegerField', [], {}),
            'transfer_sheet_id': ('django.db.models.fields.IntegerField', [], {}),
            'volume': ('django.db.models.fields.IntegerField', [], {}),
            'weight': ('django.db.models.fields.IntegerField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['public']