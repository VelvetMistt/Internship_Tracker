import { Box, Button, Container, TextField, Typography } from "@mui/material";
import { useState, useEffect } from "react";
import api from "../../api/axios";

const ProfilePage = () => {
  const [profile, setProfile] = useState({ name: "", email: "" });
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchProfile = async () => {
      const response = await api.get("/users/me");
      setProfile(response.data);
    };
    fetchProfile();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    await api.patch("/users/me", { name: profile.name });
    setMessage("Profile updated successfully.");
  };

  return (
    <Container sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Profile
      </Typography>
      <Box component="form" onSubmit={handleSubmit} sx={{ display: "grid", gap: 2, maxWidth: 500 }}>
        <TextField label="Name" value={profile.name} onChange={(e) => setProfile({ ...profile, name: e.target.value })} required />
        <TextField label="Email" value={profile.email} disabled />
        <Button type="submit" variant="contained">
          Save changes
        </Button>
        {message && (
          <Typography color="success.main" variant="body2">
            {message}
          </Typography>
        )}
      </Box>
    </Container>
  );
};

export default ProfilePage;
