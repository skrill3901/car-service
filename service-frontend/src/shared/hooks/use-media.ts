import { useMediaQuery } from 'react-responsive';

const useMedia = () => {
  const isDesktop = useMediaQuery({ minWidth: 935 });
  const isBigScreen = useMediaQuery({ minWidth: 1600 });
  const isTabletOrMobile = useMediaQuery({ maxWidth: 934 });
  const isPortrait = useMediaQuery({ orientation: 'portrait' });

  return { isDesktop, isBigScreen, isTabletOrMobile, isPortrait };
};

export default useMedia;
