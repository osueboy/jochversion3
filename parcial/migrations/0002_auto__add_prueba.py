# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Prueba'
        db.create_table('parcial_prueba', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('parcial', ['Prueba'])


    def backwards(self, orm):
        # Deleting model 'Prueba'
        db.delete_table('parcial_prueba')


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
        'parcial.prueba': {
            'Meta': {'object_name': 'Prueba'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'parcial.registro': {
            'Meta': {'object_name': 'Registro'},
            'empleado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['parcial.Empleado']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movimiento': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['parcial.Movimiento']"})
        }
    }

    complete_apps = ['parcial']