<template>
    <div class="classmateContainer">
        <el-row class="tac">
            <el-col :span="3">
                <el-menu class="scroll-container" default-active="2" @open="handleOpen" @close="handleClose">
                    <el-sub-menu index="1">
                        <template #title>
                            <el-icon>
                                <Avatar />
                            </el-icon>
                            <span>姓名</span>
                        </template>
                        <el-input v-model="keyword" placeholder="请输入姓名">
                            <template #suffix>
                                <el-icon style="cursor: pointer;" @click="search">
                                    <Search />
                                </el-icon>
                            </template>
                        </el-input>
                        <el-menu-item :index="`1-${index + 1}`" v-for="(item, index) in nameList" :key="index"
                            @click="selectStudent(item)">
                            {{ item.name }}
                            <el-tooltip content="编辑" palcement="top">
                                <el-icon class="update-icon" @click.stop="update(item)">
                                    <Edit />
                                </el-icon>
                            </el-tooltip>
                            <el-tooltip content="删除" palcement="top">
                                <el-icon class="delete-icon" @click.stop="confirmDelete(item)">
                                    <CloseBold />
                                </el-icon>
                            </el-tooltip>
                        </el-menu-item>
                    </el-sub-menu>
                    <el-sub-menu index="2"><template #title>
                            <el-icon>
                                <Menu />
                            </el-icon>
                            <span>管理</span>
                        </template>
                        <el-menu-item index="2-1" @click="CreateIPage">添加信息</el-menu-item>
                        <el-menu-item index="2-2" @click="getData">数据可视化</el-menu-item>
                    </el-sub-menu>
                </el-menu>
            </el-col>
            <el-col :span="21" class="right-content">
                <Information :selectedClassmate="selectedClassmate" /> <!-- 传递选中的同学 -->
                <GraduationMessage :selectedClassmate="selectedClassmate" />
                <Picture :selectedClassmate="selectedClassmate" />
                <Video :selectedClassmate="selectedClassmate" />
            </el-col>
        </el-row>
    </div>
    <el-dialog v-model="dialogVisible" width="70%">
        <DataVisual />
    </el-dialog>
</template>

<script>
import * as echarts from 'echarts';
import { ElMessageBox } from 'element-plus';
const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
}
const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
}

import { ref, onMounted } from 'vue';
import Navigation from '../components/Navigation.vue';
import Information from '../components/Information.vue';
import GraduationMessage from '../components/GraduationMessage.vue';
import Picture from '../components/Carousel/Picture.vue';
import Video from '../components/Carousel/Video.vue';
import DataVisual from '../components/DataVisual.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
export default {
    data() {
        return {
            dialogVisible: false,
        }
    },
    components: {
        Navigation,
        Information,
        GraduationMessage,
        Picture,
        Video,
        DataVisual,
    },
    methods: {
        // 添加信息
        CreateIPage() {
            /* 获取路由stage的值 */
            const lastRoute = this.$router.currentRoute.value.query.stage;
            this.$router.push({ path: '/classmates/createclassmate', query: { type: lastRoute } });
        },
        getData() {
            this.dialogVisible = true;
        },
        // 删除同学
        confirmDelete(item) {
            ElMessageBox.confirm(`确定删除 ${item.name} 吗？`, '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                // Handle deletion logic here
                axios.delete('/classmate/', { params: { id: item.id } }).then(
                    response => {
                        if (response.status == 200) {
                            console.log(`删除 ${item.name}成功`);
                            // 删除成功后，重新获取同学列表
                            this.$router.go(0);//刷新页面
                        } else {
                            console.log('删除失败');
                        }
                    }
                ).catch(error => {
                    console.error('删除失败:', error);
                });
            }).catch(() => {
                // Cancelled deletion
                console.log('取消删除');
            });
        },
        // 编辑同学
        update(item) {
            this.$router.push({
                path: '/classmates/updateclassmate',
                query: { id: item.id, name: item.name, type: item.classmates_album_name }
            });
        }
    },
    setup() {
        const classmatesData = ref(null);// 同学数据
        const selectedClassmate = ref(null);// 选中的同学
        const nameList = ref(null);// 姓名列表
        const searchnamelist = ref(null);// 搜索姓名列表
        const router = useRouter(); // 获取路由实例
        const keyword = ref('');// 搜索关键字
        onMounted(async () => {
            try {
                /* 获取路由最后一个字段 */
                const lastRoute = router.currentRoute.value.query.stage;
                const response = await axios.get(`/classmate/${lastRoute}`); // 替换为实际用于搜索姓名的端点
                classmatesData.value = response.data.classmates;// 获取同学列表数据
                nameList.value = response.data.classmates.map(classmate => ({ name: classmate.name, id: classmate.id, classmates_album_name: classmate.classmates_album_name }));//得到姓名列表
                if (nameList.value.length > 0) {
                    selectedClassmate.value = classmatesData.value[0];// 默认选中第一个同学
                    const firstname=selectedClassmate.value.name;
                    selectedClassmate.value = classmatesData.value.find(classmate => classmate.name === firstname);
                    selectedClassmate.value.classmates_album_path="同学录/"+lastRoute;
                    console.log('展示区selectedClassmate:', selectedClassmate.value);
                }else{
                    ElMessageBox.alert('没有匹配到同学的信息！,请到‘管理-添加信息’处添加同学信息', '提示', {
                        confirmButtonText: '确定',
                        type: 'warning'
                    });
                }
            } catch (error) {
                console.error('匹配失败:', error);
            }
        });
        const search = async () => {
            try {
                const lastRoute = router.currentRoute.value.query.stage;
                const response = await axios.get(`/classmate/${lastRoute}`); // 替换为实际用于搜索姓名的端点
                classmatesData.value = response.data.classmates;// 获取同学列表数据
                searchnamelist.value = response.data.classmates.map(classmate => ({ name: classmate.name, id: classmate.id }));
                const searchResults = searchnamelist.value.filter(classmate => {
                    return classmate.name.includes(keyword.value);
                });
                nameList.value = searchResults; // 假设这里是更新左侧列表的变量名
            } catch (error) {
                console.error('搜索失败：', error);
            }
        };
        const selectStudent = (item) => {
            const stage=router.currentRoute.value.query.stage;
            if(nameList.value.length>0){
                selectStudent.value =classmatesData.value[0];
                selectedClassmate.value = classmatesData.value.find(classmate => classmate.name === item.name);
                selectedClassmate.value.classmates_album_path="同学录/"+stage;    
            } 
        };
        return {
            selectedClassmate,
            classmatesData,
            nameList,
            searchnamelist,
            search,
            keyword,
            handleClose,
            handleOpen,
            selectStudent,
        };
    },
}
</script>

<style scoped>
.classmateContainer {
    height: calc(100vh - 80px);
}

.scroll-container {
    height: calc(100vh - 40px);
    overflow-y: auto;
}

.el-menu-item {
    cursor: pointer;
}

.el-menu-item:hover {
    border-radius: 5px;
    border: 1px solid #409EFF;
}

.update-icon,
.delete-icon {
    cursor: pointer;
    color: red;
    /* 使图标到最右侧 */
    float: right;
    margin-left: 20px;
    margin-right: 0;
}

.right-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: auto;
    width: auto;
    padding: 20px;
    background-image: linear-gradient(to right bottom, #fdf5e6, #ffe7d8, #ffd8d6, #fccbdf, #e4c4ee, #d5bff3, #c0bbf8, #a6b8fc, #abaffc, #b3a5fa, #bd99f5, #c88dee);
    overflow-y: auto;
    max-height: 100vh;
    scrollbar-width: thin;
    scrollbar-color: transparent transparent;
}

.right-content::-webkit-scrollbar {
    width: 5px;
    height: 5px;
}

.right-content::-webkit-scrollbar-thumb {
    background-color: #ccc;
    border-radius: 10px;
}
</style>