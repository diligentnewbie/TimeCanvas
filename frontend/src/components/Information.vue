<template>
    <div class="information-container">
        <div class="classmate-image">
            <img :src="classmates_avatar_name"
                style="width: 170px; height: 200px;border-radius: 50%;text-align: center;background-color: #99a9bf;" >
        </div>
        <div class="information">
            <div class="label"><i class="iconfont icon-xingming"></i>姓名</div>
            <div class="box">{{ name }}</div>
            <div class="label"><i class="iconfont icon-nicheng"></i>昵称</div>
            <div class="box">{{ nickname }}</div>
            <div class="label"><i class="iconfont icon-shengrix"></i>生日</div>
            <div class="box">{{ birthday }}</div>
            <div class="label"><i class="iconfont icon-jiaxiang"></i>家乡</div>
            <div class="box">{{ hometown }}</div>
            <div class="label"><i class="iconfont icon-QQ"></i>QQ</div>
            <div class="box">{{ qq_number }}</div>
            <div class="label"><i class="iconfont icon-weixin"></i>微信</div>
            <div class="box">{{ wx_number }}</div>
            <div class="label"><i class="iconfont icon-shouji"></i>手机</div>
            <div class="box">{{ phone_number }}</div>
            <div class="label"><i class="iconfont icon-youxiang"></i>邮箱</div>
            <div class="box">{{ email }}</div>
            <div class="label"><i class="iconfont icon-xingzuo"></i>星座</div>
            <div class="box">{{ constellation }}</div>
        </div>
        <div class="left-off">
            <div class="hobby-label">
                <i class="iconfont icon-mengxiang"></i>
                <span style="writing-mode: vertical-rl;">爱</span>
                <span style="writing-mode: vertical-rl;">好</span>
            </div>
            <div class="hobby-box">{{ hobby }}</div>
            <div class="mengxiang-label">
                <i class="iconfont icon-mengxiang"></i>
                <span style="writing-mode: vertical-rl;">梦</span>
                <span style="writing-mode: vertical-rl;">想</span>
            </div>
            <div class="mengxiang-box">{{ dream }}</div>
        </div>
        <div class="right-off"></div>
    </div>
</template>
<script lang="ts">
import { ref, PropType,watch } from 'vue';
import axios from 'axios';
export default {
    props: {
        selectedClassmate: {
            type: Object as PropType<any>,
            default: null
        },
    },
    setup(props){
        const name = ref('');
        const nickname = ref('');
        const birthday = ref('');
        const hometown = ref('');
        const hobby = ref('');
        const qq_number = ref('');
        const wx_number = ref('');
        const phone_number = ref('');
        const email = ref('');
        const constellation = ref('');
        const dream = ref('');
        const classmates_avatar_name = ref('');
        const id = ref('');
        //监听selectedClassmate的变化
        watch(() => props.selectedClassmate, (newVal) => {
            // console.log('newVal:',newVal);
            if (newVal) {
                name.value = newVal.name;
                nickname.value = newVal.nickname;
                const birthdayDate=new Date(newVal.birthday);//获取生日
                const year=birthdayDate.getFullYear();//获取年份
                const month=birthdayDate.getMonth()+1;
                const day=birthdayDate.getDate();
                birthday.value = ''+year+'年'+month+'月'+day+'日';
                hometown.value = newVal.hometown;
                hobby.value = newVal.hobby;
                qq_number.value = newVal.qq_number;
                wx_number.value = newVal.wx_number;
                phone_number.value = newVal.phone_number;
                email.value = newVal.email;
                constellation.value = newVal.constellation;
                dream.value = newVal.dream;
                classmates_avatar_name.value = newVal.classmates_avatar_name;
                id.value = newVal.id;
                // console.log('id:',id.value);
                //使用异步获取头像
                axios.get('/albumfiles',{params:{folder_name:newVal.classmates_album_path+'/'+newVal.name}})
                .then(response=>{
                    // console.log('response:',response);
                    classmates_avatar_name.value=response.data[0];
                })

            }else{
                console.log('没有匹配到同学信息！');
            }
        });
        return{
            name,
            nickname,
            birthday,
            hometown,
            hobby,
            qq_number,
            wx_number,
            phone_number,
            email,
            constellation,
            dream,
            classmates_avatar_name,
        }
    },
};
</script>

<style scoped>
.information-container {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 3fr;

    .left-off {
        grid-column: 1/3;
        display: grid;
        grid-template-columns: auto 1fr;
    }

    .right-off {
        display: none;
    }
}

.classmate-image {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 200px;
    border-radius: 8px;
    margin: 10px auto 10px;
}

.information {
    display: grid;
    grid-template-columns: 1fr 2.5fr 1fr 2.5fr;
}

.label {
    height: 20px;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.box {
    height: 20px;
    padding: 10px;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}

.hobby-label,
.mengxiang-label {
    width: auto;
    height: auto;
    background-color: #fdf5e6;
    border-radius: 8px;
    padding: 10px;
    margin: 0;
    display: flex;
    writing-mode: vertical-rl;
    align-items: center;
    margin-top: 15px;
}

.hobby-box,
.mengxiang-box {
    width: 100%;
    padding: 10px;
    margin-top: 15px;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.2);
}
</style>