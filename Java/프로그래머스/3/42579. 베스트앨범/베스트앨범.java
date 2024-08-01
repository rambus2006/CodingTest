import java.util.*;

public class Solution {
    public int[] solution(String[] genres, int[] plays) {
        // 1. 장르별 총 재생 횟수 계산
        Map<String, Integer> genrePlayCount = new HashMap<>();
        // 2. 장르별 곡 목록 작성
        Map<String, List<int[]>> genreSongs = new HashMap<>();
        
        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            genrePlayCount.put(genre, genrePlayCount.getOrDefault(genre, 0) + play);
            
            genreSongs.putIfAbsent(genre, new ArrayList<>());
            genreSongs.get(genre).add(new int[]{i, play});
        }
        
        // 3. 장르별 곡 정렬
        for (List<int[]> songs : genreSongs.values()) {
            songs.sort((a, b) -> {
                if (b[1] == a[1]) return a[0] - b[0]; // 재생 횟수가 같으면 고유 번호로 정렬
                return b[1] - a[1]; // 재생 횟수로 내림차순 정렬
            });
        }
        
        // 4. 장르별로 상위 두 곡 선택
        List<int[]> bestAlbum = new ArrayList<>();
        genrePlayCount.entrySet().stream()
            .sorted((e1, e2) -> e2.getValue() - e1.getValue()) // 총 재생 횟수로 장르 정렬
            .forEach(entry -> {
                String genre = entry.getKey();
                List<int[]> songs = genreSongs.get(genre);
                bestAlbum.add(songs.get(0));
                if (songs.size() > 1) bestAlbum.add(songs.get(1));
            });
        
        // 5. 결과 반환
        return bestAlbum.stream().mapToInt(arr -> arr[0]).toArray();
    }
}
