package com.example.email;


import javax.mail.*;
import javax.mail.internet.*;
import java.util.Properties;
import javax.swing.JOptionPane;


public class mail {
    public static void sendEmail(String to, String subject, String message) {
        String from = "your-email@example.com"; // Replace with your email address
        String password = "your-email-password"; // Replace with your email password

        Properties properties = new Properties();
        properties.put("mail.smtp.auth", "true");
        properties.put("mail.smtp.starttls.enable", "true");
        properties.put("mail.smtp.host", "smtp.example.com");
        properties.put("mail.smtp.port", "587");

        Session session = Session.getInstance(properties, new Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(from, password);
            }
        });

        try {
            MimeMessage mimeMessage = new MimeMessage(session);
            mimeMessage.setFrom(new InternetAddress(from));
            mimeMessage.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
            mimeMessage.setSubject(subject);
            mimeMessage.setText(message);

            Transport.send(mimeMessage);
            System.out.println("Email sent successfully.");
        } catch (MessagingException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        String to = "recipient@example.com";
        String subject = "Important Academic Event";
        String message = "Registration deadline is approaching. Please take action.";

        sendEmail(to, subject, message);
    }

    public static class InAppNotification {
        public static void showNotification(String message) {
            JOptionPane.showMessageDialog(null, message, "Notification", JOptionPane.INFORMATION_MESSAGE);
        }

        public static void main(String[] args) {
            String notificationMessage = "Registration deadline is approaching. Please take action.";
            showNotification(notificationMessage);
        }
    }

}
