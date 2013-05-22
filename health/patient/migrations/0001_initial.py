# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Doctor'
        db.create_table(u'patient_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('specialty', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'patient', ['Doctor'])

        # Adding model 'Disease'
        db.create_table(u'patient_disease', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'patient', ['Disease'])

        # Adding model 'Patient'
        db.create_table(u'patient_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Doctor'])),
            ('disease', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Disease'])),
        ))
        db.send_create_signal(u'patient', ['Patient'])

        # Adding model 'Equipment'
        db.create_table(u'patient_equipment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'patient', ['Equipment'])

        # Adding model 'Site'
        db.create_table(u'patient_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('equipment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Equipment'])),
        ))
        db.send_create_signal(u'patient', ['Site'])

        # Adding model 'Check'
        db.create_table(u'patient_check', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Patient'])),
        ))
        db.send_create_signal(u'patient', ['Check'])

        # Adding model 'Index'
        db.create_table(u'patient_index', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('min_value', self.gf('django.db.models.fields.FloatField')()),
            ('max_value', self.gf('django.db.models.fields.FloatField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'patient', ['Index'])

        # Adding model 'CheckItem'
        db.create_table(u'patient_checkitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('check', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Check'])),
            ('index', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Index'])),
        ))
        db.send_create_signal(u'patient', ['CheckItem'])

        # Adding model 'Comment'
        db.create_table(u'patient_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.IntegerField')()),
            ('addon', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Doctor'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient.Patient'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'patient', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Doctor'
        db.delete_table(u'patient_doctor')

        # Deleting model 'Disease'
        db.delete_table(u'patient_disease')

        # Deleting model 'Patient'
        db.delete_table(u'patient_patient')

        # Deleting model 'Equipment'
        db.delete_table(u'patient_equipment')

        # Deleting model 'Site'
        db.delete_table(u'patient_site')

        # Deleting model 'Check'
        db.delete_table(u'patient_check')

        # Deleting model 'Index'
        db.delete_table(u'patient_index')

        # Deleting model 'CheckItem'
        db.delete_table(u'patient_checkitem')

        # Deleting model 'Comment'
        db.delete_table(u'patient_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'patient.check': {
            'Meta': {'object_name': 'Check'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Patient']"})
        },
        u'patient.checkitem': {
            'Meta': {'object_name': 'CheckItem'},
            'check': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Check']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Index']"})
        },
        u'patient.comment': {
            'Meta': {'object_name': 'Comment'},
            'addon': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'content': ('django.db.models.fields.IntegerField', [], {}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Patient']"})
        },
        u'patient.disease': {
            'Meta': {'object_name': 'Disease'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {})
        },
        u'patient.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'specialty': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'patient.equipment': {
            'Meta': {'object_name': 'Equipment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'patient.index': {
            'Meta': {'object_name': 'Index'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {}),
            'min_value': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'patient.patient': {
            'Meta': {'object_name': 'Patient'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'disease': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Disease']"}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Doctor']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'patient.site': {
            'Meta': {'object_name': 'Site'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'equipment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient.Equipment']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['patient']