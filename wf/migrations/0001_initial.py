# Generated by Django 3.1.3 on 2020-12-05 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wfWorkflow',
            fields=[
                ('WorkflowId', models.CharField(db_column='workflow_id', max_length=32, primary_key=True, serialize=False, verbose_name='主键')),
                ('wfNumber', models.CharField(db_column='wf_number', max_length=12, verbose_name='工作流编号')),
                ('wfName', models.CharField(db_column='wf_name', max_length=20, verbose_name='工作流名名称')),
                ('wfStatus', models.IntegerField(db_column='wf_status', max_length=2, verbose_name='状态')),
                ('companyId', models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')),
                ('deptId', models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')),
                ('createUserId', models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')),
                ('createTime', models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')),
                ('updateUserId', models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')),
                ('updateTime', models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')),
                ('delFlag', models.IntegerField(db_column='del_flag', max_length=2, verbose_name='是否删除，1为删除，0为未删除')),
            ],
            options={
                'db_table': 't_wf_workflow',
            },
        ),
        migrations.CreateModel(
            name='wfWorkflowType',
            fields=[
                ('WorkflowTypeId', models.CharField(db_column='workflow_type_id', max_length=32, primary_key=True, serialize=False, verbose_name='主键')),
                ('orderType', models.CharField(db_column='order_type', max_length=2, verbose_name='订单类型')),
                ('companyId', models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')),
                ('deptId', models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')),
                ('createUserId', models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')),
                ('createTime', models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')),
                ('updateUserId', models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')),
                ('updateTime', models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')),
                ('delFlag', models.IntegerField(db_column='del_flag', max_length=2, verbose_name='是否删除，1为删除，0为未删除')),
                ('workflowId', models.ForeignKey(db_column='workflow_id', on_delete=django.db.models.deletion.CASCADE, to='wf.wfworkflow', verbose_name='工作流外键')),
            ],
            options={
                'db_table': 't_wf_workflow_type',
            },
        ),
        migrations.CreateModel(
            name='wfWorkflowStep',
            fields=[
                ('WorkflowStepId', models.CharField(db_column='workflow_step_id', max_length=32, primary_key=True, serialize=False, verbose_name='主键')),
                ('stepNumber', models.CharField(db_column='step_number', max_length=12, verbose_name='步骤编号')),
                ('stepName', models.CharField(db_column='step_name', max_length=20, verbose_name='步骤名称')),
                ('examParty', models.IntegerField(db_column='exam_party', max_length=2, verbose_name='审批方')),
                ('nextStep', models.CharField(db_column='next_step', max_length=300, verbose_name='下一步')),
                ('backStep', models.CharField(db_column='back_step', max_length=300, verbose_name='回退')),
                ('acceptPeople', models.CharField(db_column='accept_people', max_length=300, verbose_name='审批人')),
                ('companyId', models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')),
                ('deptId', models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')),
                ('createUserId', models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')),
                ('createTime', models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')),
                ('updateUserId', models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')),
                ('updateTime', models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')),
                ('delFlag', models.IntegerField(db_column='del_flag', max_length=2, verbose_name='是否删除，1为删除，0为未删除')),
                ('workflowId', models.ForeignKey(db_column='workflow_id', on_delete=django.db.models.deletion.CASCADE, to='wf.wfworkflow', verbose_name='工作流外键')),
            ],
            options={
                'db_table': 't_wf_workflow_step',
            },
        ),
        migrations.CreateModel(
            name='wfReplace',
            fields=[
                ('ReplaceId', models.CharField(db_column='replace_id', max_length=32, primary_key=True, serialize=False, verbose_name='主键')),
                ('number', models.CharField(db_column='number', max_length=12, verbose_name='编码')),
                ('field', models.CharField(db_column='filed', max_length=20, verbose_name='字段')),
                ('name', models.CharField(db_column='name', max_length=20, verbose_name='名称')),
                ('isDisplay', models.IntegerField(db_column='is_display', max_length=2, verbose_name='是否显示')),
                ('isChange', models.IntegerField(db_column='is_change', max_length=2, verbose_name='是否可编辑')),
                ('isNecessary', models.IntegerField(db_column='is_necessary', max_length=2, verbose_name='是否必填')),
                ('companyId', models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')),
                ('deptId', models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')),
                ('createUserId', models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')),
                ('createTime', models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')),
                ('updateUserId', models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')),
                ('updateTime', models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')),
                ('delFlag', models.IntegerField(db_column='del_flag', max_length=2, verbose_name='是否删除，1为删除，0为未删除')),
                ('workflowStepId', models.ForeignKey(db_column='workflow_step_id', on_delete=django.db.models.deletion.CASCADE, to='wf.wfworkflowstep', verbose_name='流转步骤外键')),
            ],
            options={
                'db_table': 't_wf_replace',
            },
        ),
        migrations.CreateModel(
            name='wfLog',
            fields=[
                ('peopleName', models.CharField(auto_created=True, db_column='people_name', max_length=20, verbose_name='处理人名称')),
                ('peopleNumber', models.CharField(auto_created=True, db_column='people_number', max_length=12, verbose_name='处理人编码')),
                ('logId', models.CharField(db_column='log_id', max_length=32, primary_key=True, serialize=False, verbose_name='主键')),
                ('startTime', models.DateField(db_column='start_time', max_length=6, verbose_name='处理开始时间')),
                ('endTime', models.DateField(db_column='end_time', max_length=6, verbose_name='处理结束时间')),
                ('comment', models.CharField(db_column='comment', max_length=200, verbose_name='是否可编辑')),
                ('companyId', models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')),
                ('deptId', models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')),
                ('createUserId', models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')),
                ('createTime', models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')),
                ('updateUserId', models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')),
                ('updateTime', models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')),
                ('delFlag', models.IntegerField(db_column='del_flag', max_length=2, verbose_name='是否删除，1为删除，0为未删除')),
                ('workflowId', models.ForeignKey(db_column='workflow_id', on_delete=django.db.models.deletion.CASCADE, to='wf.wfworkflow', verbose_name='工作流外键')),
                ('workflowStepId', models.ForeignKey(db_column='workflow_step_id', on_delete=django.db.models.deletion.CASCADE, to='wf.wfworkflowstep', verbose_name='流转步骤外键')),
            ],
            options={
                'db_table': 't_wf_log',
            },
        ),
    ]
