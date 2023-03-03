# DATA WARE HOUSE - DATA LAKE #

Project about Data

# Menu

* [Installation Tool](#markdown-header--nstallation-tool)
    
    * [Hadoop](#markdown-header-hadoop)

    * [Apache Spark](#markdown-header-apache-spark)

================================
# Installation Tool

Install Hadoop and Apache Spark

## Hadoop

### 1.Cập nhật hệ thống Ubuntu của bạn bằng cách sử dụng lệnh sau:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
   sudo apt update && sudo apt upgrade 
  </code></pre>
</div>

### 2.Cài đặt Java Development Kit (JDK) bằng lệnh:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  sudo apt install default-jdk
  </code></pre>
</div>

### 3.Tải xuống Hadoop

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  wget https://downloads.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
  </code></pre>
</div>

### 4.Sau khi tải xuống, giải nén file tar.gz bằng lệnh:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  tar -xzvf hadoop-3.3.4.tar.gz
  </code></pre>
</div>


### 5.Di chuyển thư mục Hadoop đã giải nén vào thư mục /usr/local bằng lệnh:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  sudo mv hadoop-3.3.4.tar.gz /usr/local/hadoop
  </code></pre>
</div>

### 6.Thiết lập biến môi trường cho Hadoop bằng cách thêm các dòng sau vào tệp tin /etc/environment:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  HADOOP_HOME=/usr/local/hadoop
    PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
  </code></pre>
</div>

### 7.Thực hiện lệnh sau để áp dụng các thay đổi cho biến môi trường:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  source /etc/environment
  </code></pre>
</div>

### 8.Sửa tệp tin cấu hình của Hadoop (file /usr/local/hadoop/etc/hadoop/hadoop-env.sh) bằng cách thêm đường dẫn của JDK vào biến JAVA_HOME như sau:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  export JAVA_HOME=/usr/lib/jvm/default-java
  </code></pre>
</div>


### 9.Cấu hình Hadoop bằng cách chỉnh sửa tệp tin /usr/local/hadoop/etc/hadoop/core-site.xml như sau:
<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
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

### 10.Chỉnh sửa tệp tin /usr/local/hadoop/etc/hadoop/hdfs-site.xml để cấu hình Hadoop để lưu trữ dữ liệu như sau:
<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
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
  </code>
  </pre>
</div>

### 11.Khởi động Hadoop bằng lệnh sau:

<div class="code-block">
  <button class="btn" data-clipboard-target="#code"></button>
  <pre><code id="code">
  /usr/local/hadoop/sbin/start-all.sh
  </code>
  </pre>
</div>

## Apache Spark
