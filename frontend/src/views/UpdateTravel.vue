<template>
    <EditT @formSubmit="handleFormSubmit" :fetchData="true" @formReset="handleFormReset" />
</template>

<script>
import EditT from '../components/EditT.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { useRoute } from 'vue-router';
export default {
    data() {
        return {
            formData: {
                travel_theme: '',//旅游主题
                travel_date: '',//旅游日期
                travel_description: '',//旅游描述
                travel_participant: '',//旅游参与者
                travel_place: '',//旅游地点
            },
        };
    },
    components: {
        EditT,
    },
    methods: {
        handleFormSubmit(newData) {
            // 在这里将表单数据传到后端
            this.formData=newData;
            console.log('formdata:',this.formData);
            /* 如果表单不完整，则返回；否则，则将数据发送给数据库 */
            if (Object.values(this.formData).some(value => !value)) 
            ElMessageBox.alert('请填写完整信息', '提示', {
                confirmButtonText: '确定',
                type: 'warning'
            });
            else{
                console.log('需要后端数据');
            };
        },
        handleFormReset() {
            console.log('reset');
            this.formData={};
        },
    },
};
</script>