# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.mysql_patch


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HanziSet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('source', libs.mysql_patch.PositiveTinyIntegerField(default=0)),
                ('hanzi_type', libs.mysql_patch.PositiveTinyIntegerField(default=0)),
                ('hanzi_char', models.CharField(default=b'', max_length=8)),
                ('hanzi_pic_id', models.CharField(default=b'', max_length=32)),
                ('variant_type', libs.mysql_patch.PositiveTinyIntegerField(default=0)),
                ('std_hanzi', models.CharField(default=b'', max_length=64)),
                ('as_std_hanzi', models.CharField(default=b'', max_length=32)),
                ('tw_seq_id', models.CharField(default=b'', max_length=32)),
                ('pinyin', models.CharField(default=b'', max_length=64)),
                ('radical', models.CharField(default=b'', max_length=8)),
                ('strokes', libs.mysql_patch.PositiveTinyIntegerField(default=0)),
                ('zheng_code', models.CharField(default=b'', max_length=32)),
                ('wubi', models.CharField(default=b'', max_length=32)),
                ('is_redundant', models.BooleanField(default=False)),
                ('dup_count', libs.mysql_patch.PositiveTinyIntegerField(default=0)),
                ('inter_dict_dup_hanzi', models.CharField(default=b'', max_length=64)),
                ('korean_dup_hanzi', models.CharField(default=b'', max_length=32)),
                ('structure', models.CharField(default=b'', max_length=16)),
                ('is_hard', models.BooleanField(default=False)),
                ('min_split', models.CharField(default=b'', max_length=256)),
                ('max_split', models.CharField(default=b'', max_length=512)),
                ('mix_split', models.CharField(default=b'', max_length=512)),
                ('deform_split', models.CharField(default=b'', max_length=256)),
                ('similar_stroke', models.CharField(default=b'', max_length=128)),
                ('stroke_serial', models.CharField(default=b'', max_length=128)),
                ('remark', models.CharField(default=b'', max_length=128)),
                ('c_t', models.DateTimeField(auto_now_add=True)),
                ('u_t', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
