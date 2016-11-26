from django.db import models

from libs.mysql_patch import PositiveTinyIntegerField

class HanziSet(models.Model):
  id = models.AutoField(primary_key=True)
  source = PositiveTinyIntegerField(default=0)
  hanzi_type = PositiveTinyIntegerField(default=0)
  hanzi_char = models.CharField(max_length=8, default='')
  hanzi_pic_id = models.CharField(max_length=32, default='')
  variant_type = PositiveTinyIntegerField(default=0)

  std_hanzi = models.CharField(max_length=64, default='')
  as_std_hanzi = models.CharField(max_length=32, default='')
  tw_seq_id = models.CharField(max_length=32, default='')
  pinyin = models.CharField(max_length=64, default='')
  radical = models.CharField(max_length=8, default='')
  strokes = PositiveTinyIntegerField(default=0)
  zheng_code = models.CharField(max_length=32, default='')
  wubi = models.CharField(max_length=32, default='')

  is_redundant = models.BooleanField(default=False)
  dup_count = PositiveTinyIntegerField(default=0)
  inter_dict_dup_hanzi = models.CharField(max_length=64, default='')
  korean_dup_hanzi = models.CharField(max_length=32, default='')

  structure = models.CharField(max_length=16, default='')
  is_hard = models.BooleanField(default=False)
  min_split = models.CharField(max_length=256, default='')
  max_split = models.CharField(max_length=512, default='')
  mix_split = models.CharField(max_length=512, default='')
  deform_split = models.CharField(max_length=256, default='')
  similar_stroke = models.CharField(max_length=128, default='')
  stroke_serial = models.CharField(max_length=128, default='')

  remark = models.CharField(max_length=128, default='')
  c_t = models.DateTimeField(auto_now_add=True)
  u_t = models.DateTimeField(auto_now=True)
