<?php
// Check if the form was submitted using the 'Submit' button
session_start();

if (isset($_GET['Submit'])) {
    $uname = $_GET['user_name'];
    $pass  = $_GET['password'];

    $servername = "localhost";
    $username   = 'root';
    $password   = '';
    $dbname     = 'ethck';

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection Failed: " . $conn->connect_error);
    }

    // This query is UNSAFE and VULNERABLE to SQL Injection
    $sql    = "SELECT * FROM login_detail WHERE user_name='$uname' AND password='$pass'";
    $result = mysqli_query($conn, $sql);
    $check  = mysqli_fetch_array($result);

    if (isset($check)) {
        $_SESSION['user_name'] = $uname;
        header("Location: new.php");
        exit(); // It's crucial to exit after a header redirect
    } else {
        echo 'Login Failed';
    }

    $conn->close();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>User Login</title>
    <style>
        html, body {
            height: 100%;
            margin: 0;
        }

        body {
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            font-family: Arial, sans-serif;
            background: #f7f7f7;
        }

        form {
            width: 320px;
            padding: 24px;
            box-shadow: 8px 8px 16px rgba(0,0,0,0.08), -2px -2px 16px rgba(0,0,0,0.04);
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            flex-direction: column;
            background: #fff;
            border-radius: 8px;
        }

        h3 {
            margin: 0 0 8px 0;
        }

        .field {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 12px;
        }

        .field label {
            font-size: 14px;
        }

        input[type="text"],
        input[type="password"] {
            border: none;
            border-bottom: 2px solid rgba(0,0,0,0.5);
            height: 36px;
            background: rgba(0,0,0,0.03);
            padding: 4px 8px;
            outline: none;
            font-size: 14px;
        }

        .actions {
            width: 100%;
            display: flex;
            justify-content: flex-end;
            gap: 8px;
        }

        input[type="submit"],
        input[type="reset"] {
            border: none;
            width: 100px;
            height: 36px;
            background: green;
            color: #fff;
            border-radius: 6px;
            cursor: pointer;
        }

        input[type="reset"] {
            background: #888;
        }

        input[type="submit"]:hover,
        input[type="reset"]:hover {
            opacity: 0.95;
        }
    </style>
</head>
<body>
    <form name="FormUser" method="get" action="">
        <h3>Login</h3>

        <div class="field">
            <label for="user_name">Username</label>
            <input type="text" id="user_name" name="user_name" required>
        </div>

        <div class="field">
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
        </div>

        <div class="actions">
            <input type="submit" name="Submit" value="Submit">
            <input type="reset" value="Reset">
        </div>
    </form>
</body>
</html>
