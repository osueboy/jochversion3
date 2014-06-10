# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movimiento'
        db.create_table('parcial_movimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('parcial', ['Movimiento'])

        # Adding model 'Empleado'
        db.create_table('parcial_empleado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aPaterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('aMaterno', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('parcial', ['Empleado'])

        # Adding model 'Registro'
        db.create_table('parcial_registro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('empleado', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['parcial.Empleado'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('movimiento', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['parcial.Movimiento'])),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('parcial', ['Registro'])


    def backwards(self, orm):
        # Deleting model 'Movimiento'
        db.delete_table('parcial_movimiento')

        # Deleting model 'Empleado'
        db.delete_table('parcial_empleado')

        # Deleting model 'Registro'
        db.delete_table('parcial_registro')


    models = {
        'parcial.empleado': {
            'Meta': {'object_name': 'Empleado'},
            'aMaterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'aPaterno': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'parcial.movimiento': {
            'Meta': {'object_name': 'Movimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'parcial.registro': {
            'Meta': {'object_name': 'Registro'},
            'empleado': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['parcial.Empleado']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movimiento': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['parcial.Movimiento']"})
        }
    }

    complete_apps = ['parcial']