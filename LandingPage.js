import { Box, Button, Container, Typography } from "@mui/material";
import { Link as RouterLink } from "react-router-dom";

const LandingPage = () => (
  <Container maxWidth="md" sx={{ py: 10 }}>
    <Typography variant="h2" gutterBottom>
      InternPilot AI
    </Typography>
    <Typography variant="h6" color="text.secondary" paragraph>
      Centralized internship application management for students. Track deadlines, interviews, and recruiter communications in one smart dashboard.
    </Typography>
    <Box sx={{ display: "flex", gap: 2, mt: 4 }}>
      <Button variant="contained" component={RouterLink} to="/register">
        Get Started
      </Button>
      <Button variant="outlined" component={RouterLink} to="/login">
        Login
      </Button>
    </Box>
  </Container>
);

export default LandingPage;
