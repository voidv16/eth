<?php
session_start();
// If user is not logged in, redirect to login page
if (!isset($_SESSION['user_name'])) {
header('Location: login.php');
exit;
}
// Safely escape username for output
$username = htmlspecialchars($_SESSION['user_name'], ENT_QUOTES |
ENT_SUBSTITUTE, 'UTF-8');
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Welcome</title>
</head>
<body>
<h1>Login Successful</h1>
<p>Welcome to the application, <strong><?php echo $username; ?></strong>.
You have logged in successfully.</p>
<a href="login.php">Log out</a>
</body>
</html>