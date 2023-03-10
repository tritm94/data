[![Hadoop](https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-ar21.svg)](https://hadoop.apache.org/)
[![ApacheSpark](https://www.vectorlogo.zone/logos/apache_spark/apache_spark-ar21.svg)](https://spark.apache.org/)

# DATA WARE HOUSE - DATA LAKE #

Project about Data

# 📝 Menu

* [Install](#markdown-header--nstallation-tool)
    
    * [Hadoop](#hadoop)

    * [Apache Spark](#apache-spark)

    * [Kafka](#)

***

## [![Hadoop](https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-ar21.svg)](https://hadoop.apache.org/)

## 🏁 **Cài đặt**

### **Cập nhật hệ thống Ubuntu**

<div class="code-block">
  <pre><code id="code">
sudo apt update && sudo apt upgrade
  </code></pre>
</div>

***
### **Cài đặt Java Development Kit (JDK)**

<div class="code-block">
  <pre><code id="code">
sudo apt install default-jdk
  </code></pre>
</div>

***
### **Tạo key cho người dùng**

#### Tạo key bằng phương thức RSA và lưu ở .ssh/id_rsa
<div class="code-block">
  <pre><code id="code">
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
  </code></pre>
</div>

#### Tạo authorized_keys (Key xác thực người dùng ở local)
<div class="code-block">
  <pre><code id="code">
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
  </code></pre>
</div>

#### Cấp quyền cho key ở .ssh/authorized_keys

<div class="code-block">
  <pre><code id="code">
chmod 0600 ~/.ssh/authorized_keys
  </code></pre>
</div>

***

#### **Tải xuống Hadoop**

<div class="code-block">
  <pre><code id="code">
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
  </code></pre>
</div>

#### Sau khi tải xuống, giải nén file tar.gz bằng lệnh:

<div class="code-block">
  <pre><code id="code">
tar -xzvf hadoop-3.3.4.tar.gz
  </code></pre>
</div>


#### Di chuyển thư mục Hadoop đã giải nén vào thư mục /usr/local bằng lệnh:

<div class="code-block">
  <pre><code id="code">
sudo mv hadoop-3.3.4.tar.gz /usr/local/hadoop
  </code></pre>
</div>

***

### **Thiết lập biến môi trường cho Hadoop**

#### Trỏ vào file theo đường dẫn /etc/environment

```
sudo vi /etc/environment
```

#### Thêm các dòng sau vào tệp tin /etc/environment

<div class="code-block">
  <pre><code id="code">
HADOOP_HOME=/usr/local/hadoop
PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
  </code></pre>
</div>

#### Thực hiện lệnh sau để áp dụng các thay đổi cho biến môi trường:

<div class="code-block">
  <pre><code id="code">
source /etc/environment
  </code></pre>
</div>

***

### **Cấu hình Hadoop**

#### Sửa tệp tin cấu hình của Hadoop (file /usr/local/hadoop/etc/hadoop/hadoop-env.sh) bằng cách thêm đường dẫn của JDK vào biến JAVA_HOME như sau:

<div class="code-block">
  <pre><code id="code">
export JAVA_HOME=/usr/lib/jvm/default-java
  </code></pre>
</div>


#### Cấu hình Hadoop bằng cách chỉnh sửa tệp tin /usr/local/hadoop/etc/hadoop/core-site.xml như sau:
<div class="code-block">
  <pre><code id="code">
&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;fs.defaultFS&lt;/name&gt;
    &lt;value&gt;hdfs://localhost:9000&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
  </code>
  </pre>
</div>

#### Chỉnh sửa tệp tin /usr/local/hadoop/etc/hadoop/hdfs-site.xml để cấu hình Hadoop để lưu trữ dữ liệu như sau:
<div class="code-block">
  <pre><code id="code">
&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;dfs.replication&lt;/name&gt;
    &lt;value&gt;1&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;dfs.namenode.name.dir&lt;/name&gt;
    &lt;value&gt;/usr/local/hadoop/hadoop_data/hdfs/namenode&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;dfs.datanode.data.dir&lt;/name&gt;
    &lt;value&gt;/usr/local/hadoop/hadoop_data/hdfs/datanode&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
  </code></pre>
</div>

#### Chỉnh sửa tệp tin /usr/local/hadoop/etc/hadoop/mapred-site.xml để cấu hình Hadoop để lưu trữ dữ liệu như sau:
<div class="code-block">
  <pre><code id="code">
&lt;configuration&gt;
  &lt;property&gt;
    &lt;name>mapreduce.framework.name&lt;/name&gt;
    &lt;value&gt;yarn&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
  </code>
  </pre>
</div>

#### Chỉnh sửa tệp tin /usr/local/hadoop/etc/hadoop/yarn-site.xml để cấu hình Hadoop để lưu trữ dữ liệu như sau:
<div class="code-block">
  <pre><code id="code">
&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;yarn.nodemanager.aux-services&lt;/name&gt;
    &lt;value&gt;mapreduce_shuffle&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;yarn.nodemanager.aux-services.mapreduce.shuffle.class&lt;/name&gt;
    &lt;value&gt;org.apache.hadoop.mapred.ShuffleHandler&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;yarn.resourcemanager.hostname&lt;/name&gt;
    &lt;value&gt;127.0.0.1&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;yarn.acl.enable&lt;/name&gt;
    &lt;value&gt;0&lt;/value&gt;
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;yarn.nodemanager.env-whitelist&lt;/name&gt;&nbsp;&nbsp;&nbsp;
  &lt;value&gt;JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PERPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
  </code>
  </pre>
</div>

***

### **Định dạng HDFS nghe mới khởi chạy hadoop lần đầu**

<div class="code-block">
  <pre><code id="code">
hdfs namenode -format
  </code></pre>
</div>

#### Nếu SSH daemon chưa được cài đặt, bạn có thể cài đặt nó bằng lệnh sau:

<div class="code-block">
  <pre><code id="code">
sudo apt-get install openssh-server
  </code></pre>
</div>

#### Sau khi cài đặt xong, chạy lệnh sau để kiểm tra trạng thái của SSH daemon:

<div class="code-block">
  <pre><code id="code">
12sudo service ssh start
  </code></pre>
</div>

#### Kiểm tra lại SSH daemon.

<div class="code-block">
  <pre><code id="code">
sudo service ssh status
  </code></pre>
</div>


#### Khởi động Hadoop bằng lệnh sau:
```
$HADOOP_HOME/sbin/start-all.sh
```

#### :smile: Khởi chạy được Data Node và Name Node trong Hadoop

#### Data Node: http://localhost:9864
#### Name Node: http://localhost:9870

***

## [![Apache Spark](https://spark.apache.org/images/spark-logo-rev.svg)](https://spark.apache.org/)

## 🏁 **Cài đặt**

### **Cập nhật hệ thống Ubuntu**

<div class="code-block">
  <pre><code id="code">
sudo apt update && sudo apt upgrade
  </code></pre>
</div>

***
### **Cài đặt Java Development Kit (JDK)**

<div class="code-block">
  <pre><code id="code">
sudo apt install default-jdk
  </code></pre>
</div>

#### **Tải xuống Apache Spark**

<div class="code-block">
  <pre><code id="code">
wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3-scala2.13.tgz
  </code></pre>
</div>

#### Sau khi tải xuống, giải nén file tar.gz bằng lệnh:

<div class="code-block">
  <pre><code id="code">
tar -xzvf spark-3.3.2-bin-hadoop3-scala2.13.tgz
  </code></pre>
</div>


#### Di chuyển thư mục Apache Spark đã giải nén vào thư mục /usr/local bằng lệnh:

<div class="code-block">
  <pre><code id="code">
sudo mv spark-3.3.2-bin-hadoop3-scala2.13 /usr/local/spark
  </code></pre>
</div>

***

### **Thiết lập biến môi trường cho Spark**

#### Trỏ vào file theo đường dẫn /etc/environment

```
sudo vi /etc/environment
```

#### Thêm các dòng sau vào tệp tin /etc/environment

<div class="code-block">
  <pre><code id="code">
SPARK_HOME=/usr/local/spark
PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
  </code></pre>
</div>

#### Thực hiện lệnh sau để áp dụng các thay đổi cho biến môi trường:

<div class="code-block">
  <pre><code id="code">
source /etc/environment
  </code></pre>
</div>

***

#### Khởi động master spark bằng lệnh sau:
```
$SPARK_HOME/sbin/start-master.sh
```

#### Kiểm tra Spark đã khởi chạy: http://172.31.129.237:8080/

***

#### Khởi động cluster spark bằng lệnh sau:
```
$SPARK_HOME/sbin/start-worker.sh spark://localhost:7077
```

#### Kiểm tra Spark đã khởi chạy: http://172.31.129.237:8080/