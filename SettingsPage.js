import { Box, Container, Switch, FormControlLabel, Typography } from "@mui/material";
import { useState } from "react";

const SettingsPage = () => {
  const [darkMode, setDarkMode] = useState(true);

  return (
    <Container sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Settings
      </Typography>
      <Box>
        <FormControlLabel
          control={<Switch checked={darkMode} onChange={(event) => setDarkMode(event.target.checked)} />}
          label="Dark mode"
        />
      </Box>
      <Typography color="text.secondary" sx={{ mt: 2 }}>
        Customize your account preferences, notification settings, and dashboard display options.
      </Typography>
    </Container>
  );
};

export default SettingsPage;
