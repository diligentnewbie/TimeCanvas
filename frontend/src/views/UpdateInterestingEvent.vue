<template>
    <EditI @formSubmit="handleFormSubmit" :fetchData="true" @formReset="handleFormReset" />
</template>

<script>
import EditI from '../components/EditI.vue';
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { useRoute } from 'vue-router';
export default {
    data() {
        return {
            formData: {
                event_name: '',
                event_date: '',
                event_description: '',
                event_participant: '',
            },
        };
    },
    components: {
        EditI,
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
                console.log('更新趣事录成功');
            };
        },
        handleFormReset() {
            console.log('reset');
            this.formData={};
        },
    },
};
</script>